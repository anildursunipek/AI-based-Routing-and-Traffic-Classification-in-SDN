from mininet.log import setLogLevel
from mininet.topo import MinimalTopo
from mininet.net import Mininet

if __name__ == '__main__':
    setLogLevel( 'info' )
    topo = MinimalTopo()
    net = Mininet(topo=topo)
    net.start()
    net.stop()