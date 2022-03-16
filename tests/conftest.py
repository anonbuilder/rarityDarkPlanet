import pytest
from brownie import Contract
#import os
#os.environ["FTMSCAN_TOKEN"] = "FTMSCAN_API"


@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


@pytest.fixture(scope="module")
def deployer(accounts):
    yield accounts[0]


@pytest.fixture(scope="module")
def alice(accounts):
    yield accounts[1]


@pytest.fixture(scope="module")
def bob(accounts):
    yield accounts[2]


@pytest.fixture(scope="module")
def keeper(accounts):
    yield accounts[3]


@pytest.fixture(scope="module")
def dcm(deployer, DaycareManager):
    yield deployer.deploy(DaycareManager)


@pytest.fixture(scope="module")
def adventuretime():
   #yield Contract.from_explorer('0x0D4C98901563ca730332e841EDBCB801fe9F2551')
   yield Contract("0x0D4C98901563ca730332e841EDBCB801fe9F2551")

@pytest.fixture(scope="module")
def rarity():
    #yield Contract.from_explorer('0xce761D788DF608BD21bdd59d6f4B54b2e27F25Bb')
    yield Contract("0xce761D788DF608BD21bdd59d6f4B54b2e27F25Bb")
    
@pytest.fixture(scope="module")
def spooky_router():
    #yield Contract.from_explorer('0xf491e7b69e4244ad4002bc14e878a34207e38c29')
    yield Contract("0xce761D788DF608BD21bdd59d6f4B54b2e27F25Bb")
    
@pytest.fixture(scope="module")
def dp_token():
    #yield Contract.from_explorer('0x08B1c9A96c663EE1E0cD7029F13aceD7dcF5e373')
    yield Contract("0x08B1c9A96c663EE1E0cD7029F13aceD7dcF5e373")
        
@pytest.fixture(scope="module")
def spooky_router():
    #yield Contract.from_explorer('0xf491e7b69e4244ad4002bc14e878a34207e38c29')
    yield Contract("0xf491e7b69e4244ad4002bc14e878a34207e38c29")    
        
@pytest.fixture(scope="module")
def dp_masterchef():
    #yield Contract.from_explorer('0xa2920Cebe8d86C7EB5dF48BCc5B9d603Ff73f4D9')
    yield Contract("0xa2920Cebe8d86C7EB5dF48BCc5B9d603Ff73f4D9")
    
