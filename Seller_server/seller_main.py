import logging, sys, pickle, socket
import asyncio
import grpc
import items_pb2_grpc
import database
from database.item_master import ItemMasterServicer
from config import init_current_server_number, init_raft_seller, init_sql_alchemy_obj, get_current_server_number, \
    init_udp_port, insert_into_sequence_messages, insert_into_request_messages, get_messages_dict, set_global_sequence_number


async def serve(item_master_servicer) -> None:
    server = grpc.aio.server()
    await database.connect_db(get_current_server_number())
    items_pb2_grpc.add_ItemMasterServicer_to_server(servicer=item_master_servicer, server=server)
    grpc_port_number = int(sys.argv[3])
    listen_addr = '0.0.0.0:' + str(grpc_port_number)
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        # Shuts down the server with 0 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(0)


async def listen_on_udp():
    from config import init_sock
    init_udp_port(int(sys.argv[2]))
    init_sock()
    from config import sock
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            request_data = pickle.loads(data)
            if request_data.get('message_type') == 'request_msg':
                # print("this is a request message :- ",  request_data)
                method_name = request_data['method_name']
                await getattr(item_master_servicer, method_name)(request=request_data, context='origin_server')

            elif request_data.get('message_type') == 'sequence_msg':
                # check the sequence message conditions 4 in the google sheet
                # print("this is a sequence message :- ", request_data)
                insert_into_sequence_messages(request_data.get('global'), ((request_data.get('sid'),
                                                                            request_data.get('seq')),
                                                                            'metadata'))
                request_msg_dict_val = get_messages_dict('local')[(request_data.get('sid'), request_data.get('seq'))]
                request_msg_dict_val['global'] = request_data.get('global')
                # print("changed request_dict_val :- ", request_msg_dict_val)
                # print("change in request_messages_dict :- ", get_messages_dict('local'))

                set_global_sequence_number(request_data.get('global') + 1)

            elif request_data.get('message_type') == 'retransmit_resp':
                sequence_message_number = request_data.get('sequence_message_number')
                print("Received retransmit_resp response for sequence number :- ", sequence_message_number)
                seq_msg = request_data.get('seq_msg')
                req_msg = request_data.get('req_msg')
                insert_into_sequence_messages(sequence_message_number, seq_msg[sequence_message_number])
                insert_into_request_messages(seq_msg[sequence_message_number][0], req_msg[seq_msg[sequence_message_number][0]])

            else:

                sequence_number = request_data.get('sequence_message_number')
                print("processing retransmit request for sequence number :- ", sequence_number)
                seq_msg = get_messages_dict('global')[sequence_number]
                req_msg = get_messages_dict('local')[seq_msg[0]]
                seq_msg_dict = {sequence_number: seq_msg}
                req_msg_dict = {seq_msg[0]: req_msg}
                print("seq_msg_dict is :- ", seq_msg_dict)
                print("-------------------------------------------------------------")
                print("req_msg_dict is :- ", req_msg_dict)
                print("-------------------------------------------------------------")

                send_message = {'seq_msg': seq_msg_dict, 'req_msg': req_msg_dict, 'sequence_message_number': sequence_number,
                                'message_type': 'retransmit_resp'}
                send_message = pickle.dumps(send_message)
                sock.sendto(send_message, addr)

        except socket.timeout:
            print("", end="")
        await asyncio.sleep(1)


if __name__ == '__main__':
    item_master_servicer = ItemMasterServicer()
    init_current_server_number(int(sys.argv[1]))
    init_sql_alchemy_obj()

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    init_raft_seller()

    loop.create_task(serve(item_master_servicer))
    loop.create_task(listen_on_udp())
    loop.run_forever()
