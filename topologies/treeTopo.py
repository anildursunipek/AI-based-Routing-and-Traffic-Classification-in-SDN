from mininet.log import setLogLevel
from mininet.node import OVSSwitch
from mininet.topolib import TreeNet

if __name__ == '__main__':
    setLogLevel( 'info' )
    network = TreeNet( depth=2, fanout=4, switch=OVSSwitch, waitConnected=True)
    network.start()
    