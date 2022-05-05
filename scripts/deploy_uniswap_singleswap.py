# from scripts.helpful_scripts import get_account, get_contract
# from brownie import Lottery, config, network

# def deploy_lottery():
#     account = get_account(id="testing")
#     lottery = Lottery.deploy(
#         get_contract("eth_usd_price_feed").address,
#         get_contract("vrf_coordinator").address,
#         get_contract("link_token").address,
#         config["networks"][network.show_active()]["fee"],
#         config["networks"][network.show_active()]["keyhash"],
#         {"from": account},
#         publish_source = config["networks"][network.show_active()].get("verify", False)
#     )
#     print("Deployed lottery!")

# def main():
#     deploy_lottery()

################################################################################################
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