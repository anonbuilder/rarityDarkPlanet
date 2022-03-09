import click
from brownie import accounts, DaycareManager, network

global dcm

def main():
    print(f"Deploying to '{network.show_active()}' network")
    return DaycareManager.deploy({"from": accounts[0]})
