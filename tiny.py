import log,algo
from tinyman.v1.client import TinymanMainnetClient

assetIDMap={"ALGO":0,"YLDY":226701642}
client=TinymanMainnetClient(user_address=algo.account["address"])

def getAsset(asset):return client.fetch_asset(assetIDMap[asset])
def getPool(trgAsset,srcAsset):return client.fetch_pool(trgAsset,srcAsset)
def getQuote(pool,asset,amount):return pool.fetch_fixed_input_swap_quote(asset(amount),slippage=0.01)

def swap(quote):
	log.out("Converting {} {} to {} {} on tinyman".format(
                quote.amount_in.amount/1000000,
		quote.amount_in.asset.name,
                quote.amount_out.amount/1000000,
		quote.amount_out.asset.name
                ))
	transaction_group=pool.prepare_swap_transactions_from_quote(quote)
	transaction_group.sign_with_private_key(algo.account["address"],algo.account["private_key"])
	result=client.submit(transaction_group,wait=True)

def getSwapAmount():
	data=algo.getWalletData(algo.account["address"])
	return algo.getAvailableBalance(data)/2
	

def swap_fake(quote):
	log.out("Converting {} {} to {} {} on tinyman".format(
		quote.amount_in.amount/1000000,
                quote.amount_in.asset.name,
                quote.amount_out.amount/1000000,
                quote.amount_out.asset.name
		))




