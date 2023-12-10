from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSSwitch
from mininet.topo import LinearTopo
from mininet.net import Mininet

if __name__ == '__main__':
    setLogLevel( 'info' )
    topo = LinearTopo(2,3)
    net = Mininet(topo=topo)
    net.start()