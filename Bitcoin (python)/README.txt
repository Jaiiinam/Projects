Note: This code is a JSON powered project. Hence, use a postman type application or a browser (FireFox provides cleaner output) is needed

Run the given code and then do as following:

This link will create wallets which has an account id and a balance (10 initial amount):
http://127.0.0.1:8080/create_wallets

This link will automatically create 10 to 20 transactions among the wallet accounts:
http://127.0.0.1:8080/create_transactions

This link will show balances in each account (do this after transactions are made to see the changes):
http://127.0.0.1:8080/show_balances

Mempool bascially holds all transactions until a block is mined:
http://127.0.0.1:8080/show_mempool

In bitcoin people will generally have to solve a puzzle to be able to mine a block 
However, it is not the case here, you can simply use the link below which will mine a block for you:
http://127.0.0.1:8080/mine_block

Once a block is mined you can use the following link to see all the blocks in the blockchain 
http://127.0.0.1:8080/get_blocks

Or you can look for specific block just by entering a block number
http://127.0.0.1:8080/get_block?block=1

You should also use the following link to check if the whole blockchain is fine (checks merkle root and looks for previous block hash):
http://127.0.0.1:8080/check_blockchain