from mininet.log import setLogLevel
from mininet.topo import SingleSwitchReversedTopo
from mininet.net import Mininet

if __name__ == '__main__':
    setLogLevel( 'info' )
    topo = SingleSwitchReversedTopo(5)
    net = Mininet(topo=topo)
    net.start()