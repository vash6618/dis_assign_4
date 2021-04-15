# Programming Assignment 4
# People involved in the assignment :- 
# Vasu Sharma and Manan Khasgiwale

# Current state of the system
    Clients are running on terminal.
    Clients access the respective proxy/frontend servers via rest calls to load balancer.
    The frontend server calls the backend db layer via grpc calls. This also happens via a load 
    balancer on top of db layer. 
    The are three instances each of customer and product database running on Cloud SQL (Postgre). 
    Each server interacts with each db instance. 
    Raft is running for the product database calls and Rotating Sequencer ABP is running for 
    customer database calls.

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

    Average response time for each client function when one server-side sellers interface replica and 
    one server side buyers interface to which some of the clients are connected fail.
       Seller APIs
            1) Create Seller Account: 1499.99 ms
            2) Login using Seller Account: 224.239 ms
            3) Logout: 145.294 ms
            4) Put an item for sale: 1322.2469 ms
            5) Change the sale price of an item: 1607.033 ms
            6) Remove an item for sale: 427.188 ms
            7) Display items currently on sale put up by this seller: 659.877 ms
            8) Get seller rating: 253.307 ms

        Buyer APIs
             1) Create Buyer Account: 1819.93 ms
             2) Login using Buyer Account: 2157.1189 ms
             3) Logout: 140.996 ms
             4) Search items for sale: 536.93 ms
             5) Add item to the shopping cart: 1752.93 ms
             6) Remove item from the shopping cart: 250.567 ms
             7) Clear the shopping cart: 205.098 ms
             8) Display the shopping cart: 1864.92 ms
             9) Make purchase: 4661.329 ms
            10) Provide feedback: 2356.8889 ms
            11) Get Seller rating: 2177.232 ms
            12) Get Purchase history: 1996.826 ms

    Average response time for each client function when one product database replica (not the leader) fails.
       Seller APIs
            1) Create Seller Account: 405.594 ms
            2) Login using Seller Account: 1154.538 ms
            3) Logout: 69.406 ms
            4) Put an item for sale: 454.423 ms
            5) Change the sale price of an item: 418.366 ms
            6) Remove an item for sale: 1378.5829 ms
            7) Display items currently on sale put up by this seller: 390.518 ms
            8) Get seller rating: 389.079 ms

        Buyer APIs
             1) Create Buyer Account: 1371.832 ms
             2) Login using Buyer Account: 931.579 ms
             3) Logout: 58.656 ms
             4) Search items for sale: 334.937  ms
             5) Add item to the shopping cart: 7031.433 ms/288.56 ms
             6) Remove item from the shopping cart: 2332.545 ms
             7) Clear the shopping cart: 395.149 ms
             8) Display the shopping cart: 1576.852 ms
             9) Make purchase: 2277.727 ms
            10) Provide feedback: 1765.867 ms
            11) Get Seller rating: 180.575 ms
            12) Get Purchase history: 1012.578 ms


    Average response time for each client function when the product database replica acting as leader fails.
       Seller APIs
            1) Create Seller Account: 2325.85 ms
            2) Login using Seller Account: 199.505 ms
            3) Logout: 64.794 ms
            4) Put an item for sale: 1711.973 ms
            5) Change the sale price of an item: 1352.121 ms
            6) Remove an item for sale: 1199.219 ms
            7) Display items currently on sale put up by this seller: 396.707 ms
            8) Get seller rating: 212.994 ms

        Buyer APIs
             1) Create Buyer Account: 1716.159 ms
             2) Login using Buyer Account: 215.579 ms
             3) Logout: 70.304 ms
             4) Search items for sale: 1991.684  ms
             5) Add item to the shopping cart: 652.707 ms
             6) Remove item from the shopping cart: 1017.937 ms
             7) Clear the shopping cart: 1659.025 ms
             8) Display the shopping cart: 984.212 ms
             9) Make purchase: 2904.433 ms
            10) Provide feedback: 2407.712 ms
            11) Get Seller rating: 181.038 ms
            12) Get Purchase history: 374.473 ms
