from brownie import accounts
from scripts.deploy_uniswap_singleswap import deploy_uniswap_singleswap

# def test_account_balance():
#     balance = accounts[1].balance()
#     accounts[1].transfer(accounts[0], "1 ether", gas_price=0)
#     assert balance - "1 ether" == accounts[1].balance()

def test_uniswap_swapexample():
    # arrange 
    account = accounts[0]
    DAI = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
    WETH = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    DAI_WHALE = '0x9a315bdf513367c0377fb36545857d12e85813ef'
    AMOUNT_IN = 1 * (10 ** 18) * (10 ** 6)
    # dai IERC20 contract
        # approve(account, AMOUNT_IN, {"from": account})
    single_swap = deploy_uniswap_singleswap()
    AMOUNT_IN = 1
    # act 
    tx = single_swap.swapExactInputSingle(AMOUNT_IN, {"from": account})
    tx.wait(1)
    # assert 
    # print(single_swap.swapExactInputSingle(AMOUNT_IN, {"from": account}))