#!/usr/bin/python

import os
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.util import irange

HOME_FOLDER = os.getenv('HOME')

class LinearTopo(Topo):
    """
    construct a network of N hosts and N-1 switches, connected as follows:
    h1 <-> s1 <-> s2 .. sN-1
           |       |    |
           h2      h3   hN

    """
    def __init__(self, N, **params):
        Topo.__init__(self, **params)

        hosts = [ self.addHost( 'h%s' % h )
                  for h in irange( 1, N ) ]

        switches = [ self.addSwitch( 's%s' % s, protocols=["OpenFlow13"] )
                     for s in irange( 1, N - 1 ) ]

        # Wire up switches
        last = None
        for switch in switches:
            if last:
                self.addLink( last, switch )
            last = switch

        # Wire up hosts
        self.addLink( hosts[ 0 ], switches[ 0 ] )
        for host, switch in zip( hosts[ 1: ], switches ):
            self.addLink( host, switch )

def startNetworkWithLinearTopo( hostCount ):
    global net
    net = Mininet(topo=LinearTopo(hostCount), build=False)

    remote_ip = "127.0.0.1"
    info('** Adding Floodlight Controller\n')
    net.addController('c1', controller=RemoteController,
                      ip=remote_ip, port=6653)

    # Build the network
    net.build()
    net.start()

def stopNetwork():
    if net is not None:
        info('** Tearing down network\n')
        net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    startNetworkWithLinearTopo(6)
    CLI(net)
    stopNetwork()