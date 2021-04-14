# Programming Assignment 4
# People involved in the assignment :- 
# Vasu Sharma and Manan Khasgiwale

# Current state of the system
    Clients are running on terminal.
    Clients access the respective proxy/frontend servers via rest calls to load balancer.
    The frontend server calls the backend db layer via grpc calls. This also happens via a load balancer on top of db layer. 
    The are three instances each of customer and product database running on Cloud SQL(Postgre). Each server interacts with each db instance. 
    Raft is running for the product database calls and Rotating Sequencer ABP is running for customer database calls.

# Assumptions
    # 

# How to run
    Run the instances for product and customer database.
    Run the respective servers on google cloud.
    Connect to cloud via buyer/seller client from terminal.

# Round trip latencies for APIs
    Average response time for each client function when all replicas run normally (no failures).
        Seller APIs
            1) Create Seller Account: 786.277 ms
            2) Login using Seller Account: 215.585 ms/1532.637 ms/2495.447 ms
            3) Logout: 80.294 ms
            4) Put an item for sale: 3277.946 ms/871.007 ms
            5) Change the sale price of an item: 1292.639 ms
            6) Remove an item for sale: 2802.401 ms/495.714 ms
            7) Display items currently on sale put up by this seller: 1342.939 ms/182.846 ms
            8) Get seller rating: 880.868 ms

        Buyer APIs
             1) Create Buyer Account: 2375.653 ms
             2) Login using Buyer Account: 1103.812 ms
             3) Logout: 72.568 ms
             4) Search items for sale: 2168.963  ms
             5) Add item to the shopping cart: 1859.209 ms
             6) Remove item from the shopping cart: 260.741 ms
             7) Clear the shopping cart: 955.302 ms
             8) Display the shopping cart: 1139.147 ms
             9) Make purchase: 5392.808 ms/1495.673 ms
            10) Provide feedback: 726.948 ms
            11) Get Seller rating: 394.936 ms
            12) Get Purchase history: 1061.613 ms

    Average response time for each client function when one server-side sellers interface replica and one server side buyers interface to which some of the clients are connected fail.
       Seller APIs
            1) Create Seller Account: 464.261 ms
            2) Login using Seller Account: 215.585 ms
            3) Logout: 145.294 ms
            4) Put an item for sale: 422.679 ms
            5) Change the sale price of an item: 228.51 ms
            6) Remove an item for sale: 288.625 ms
            7) Display items currently on sale put up by this seller: 215.904 ms
            8) Get seller rating: 211.828 ms

        Buyer APIs
             1) Create Buyer Account: 404.968 ms
             2) Login using Buyer Account: 221.506 ms
             3) Logout: 140.996 ms
             4) Search items for sale: 526.507 ms
             5) Add item to the shopping cart: 471.546 ms
             6) Remove item from the shopping cart: 444.972 ms
             7) Clear the shopping cart: 208.482 ms
             8) Display the shopping cart: 258.078 ms
             9) Make purchase: 792.865 ms
            10) Provide feedback: 467.861 ms
            11) Get Seller rating: 185.848 ms
            12) Get Purchase history: 267.284 ms

    Average response time for each client function when one product database replica (not the leader) fails.
       Seller APIs
            1) Create Seller Account: 464.261 ms
            2) Login using Seller Account: 215.585 ms
            3) Logout: 145.294 ms
            4) Put an item for sale: 422.679 ms
            5) Change the sale price of an item: 228.51 ms
            6) Remove an item for sale: 288.625 ms
            7) Display items currently on sale put up by this seller: 215.904 ms
            8) Get seller rating: 211.828 ms

        Buyer APIs
             9) Make purchase: 792.865 ms

    Average response time for each client function when the product database replica acting as leader fails.
       Seller APIs
            1) Create Seller Account: 464.261 ms
            2) Login using Seller Account: 215.585 ms
            3) Logout: 145.294 ms
            4) Put an item for sale: 422.679 ms
            5) Change the sale price of an item: 228.51 ms
            6) Remove an item for sale: 288.625 ms
            7) Display items currently on sale put up by this seller: 215.904 ms
            8) Get seller rating: 211.828 ms

        Buyer APIs
             9) Make purchase: 792.865 ms