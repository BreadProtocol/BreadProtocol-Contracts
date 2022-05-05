from brownie import SwapExamples, accounts

def deploy_swaprouter():
    pass

def deploy_uniswap_singleswap():
    account = accounts[0]
    single_swap = SwapExamples.deploy(
        '0xE592427A0AEce92De3Edee1F18E0157C05861564',
        {"from": account}
    )
def main():
    deploy_uniswap_singleswap()