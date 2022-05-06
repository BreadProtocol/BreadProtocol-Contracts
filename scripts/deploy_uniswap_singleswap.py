from brownie import SwapExamples, accounts, interface
from web3 import Web3
from scripts.get_weth import get_weth

def approve_erc20(amount, single_swap_address, erc20_address, account):
    # approve the WETH token to be swapped with Uniswap
    print("Approving ERC20...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(single_swap_address, amount, {"from": account})
    tx.wait(1)
    print("Approved!")

def deploy_uniswap_singleswap():
    account = accounts[0]
    single_swap = SwapExamples.deploy(
        '0xE592427A0AEce92De3Edee1F18E0157C05861564',
        {"from": account}
    )
    print(f"Deployed single swap to {single_swap.address}!")
    return single_swap

def main():
    account = accounts[0]
    # WETH address
    erc20_address = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
    amount = Web3.toWei(0.1, "ether")
    print("Getting WETH...")
    get_weth(account)
    single_swap = deploy_uniswap_singleswap()
    approve_erc20(amount, single_swap.address, erc20_address, account)
    print("Swapping...")
    tx = single_swap.swapExactInputSingle(amount, {"from": account})
    tx.wait(1)
    print("Done with swap!")