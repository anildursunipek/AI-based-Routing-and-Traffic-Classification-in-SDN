#!/usr/bin/python

import time
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.topo import Topo
from mininet.link import TCLink

class NsfnetTopo(Topo):
    """
    Topology Link: https://github.com/BNN-UPC/NetworkModelingDatasets/blob/master/assets/nsfnet_topology.png
    """
    def build( self, **params ):
        # Hosts
        h0 = self.addHost('h0', ip='10.0.0.1')
        h1 = self.addHost('h1', ip='10.0.0.2')
        h2 = self.addHost('h2', ip='10.0.0.3')
        h3 = self.addHost('h3', ip='10.0.0.4')
        h4 = self.addHost('h4', ip='10.0.0.5')
        h5 = self.addHost('h5', ip='10.0.0.6')
        h6 = self.addHost('h6', ip='10.0.0.7')
        h7 = self.addHost('h7', ip='10.0.0.8')
        h8 = self.addHost('h8', ip='10.0.0.9')
        h9 = self.addHost('h9', ip='10.0.0.10')
        h10 = self.addHost('h10', ip='10.0.0.11')
        h11 = self.addHost('h11', ip='10.0.0.12')
        h12 = self.addHost('h12', ip='10.0.0.13')
        h13 = self.addHost('h13', ip='10.0.0.14')

        # Switches
        s0 = self.addSwitch('s0', dpid='00:00:00:00:00:00:00:01', protocols="OpenFlow13")
        s1 = self.addSwitch('s1', dpid='00:00:00:00:00:00:00:02', protocols="OpenFlow13")
        s2 = self.addSwitch('s2', dpid='00:00:00:00:00:00:00:03', protocols="OpenFlow13")
        s3 = self.addSwitch('s3', dpid='00:00:00:00:00:00:00:04', protocols="OpenFlow13")
        s4 = self.addSwitch('s4', dpid='00:00:00:00:00:00:00:05', protocols="OpenFlow13")
        s5 = self.addSwitch('s5', dpid='00:00:00:00:00:00:00:06', protocols="OpenFlow13")
        s6 = self.addSwitch('s6', dpid='00:00:00:00:00:00:00:07', protocols="OpenFlow13")
        s7 = self.addSwitch('s7', dpid='00:00:00:00:00:00:00:08', protocols="OpenFlow13")
        s8 = self.addSwitch('s8', dpid='00:00:00:00:00:00:00:09', protocols="OpenFlow13")
        s9 = self.addSwitch('s9', dpid='00:00:00:00:00:00:00:10', protocols="OpenFlow13")
        s10 = self.addSwitch('s10', dpid='00:00:00:00:00:00:00:11', protocols="OpenFlow13")
        s11 = self.addSwitch('s11', dpid='00:00:00:00:00:00:00:12', protocols="OpenFlow13")
        s12 = self.addSwitch('s12', dpid='00:00:00:00:00:00:00:13', protocols="OpenFlow13")
        s13 = self.addSwitch('s13', dpid='00:00:00:00:00:00:00:14', protocols="OpenFlow13")

        # Links
        # Link options
        linkopts1 = dict(delay='25ms', bw=100, loss=0, max_queue_size=1000, use_htb=True) # between switch and host
        linkopts2 = dict(delay='25ms', bw=100, loss=0, max_queue_size=2000, use_htb=True) # between 2 switches

        # Switch to switch
        self.addLink(s0, s1, **linkopts2)
        self.addLink(s0, s2, **linkopts2)
        self.addLink(s0, s3, **linkopts2)
        self.addLink(s1, s7, **linkopts2)
        self.addLink(s1, s2, **linkopts2)
        self.addLink(s2, s5, **linkopts2)
        self.addLink(s3, s4, **linkopts2)
        self.addLink(s3, s8, **linkopts2)
        self.addLink(s4, s5, **linkopts2)
        self.addLink(s4, s6, **linkopts2)
        self.addLink(s5, s12, **linkopts2)
        self.addLink(s5, s13, **linkopts2)
        self.addLink(s6, s7, **linkopts2)
        self.addLink(s7, s10, **linkopts2)
        self.addLink(s8, s9, **linkopts2)
        self.addLink(s8, s11, **linkopts2)
        self.addLink(s9, s10, **linkopts2)
        self.addLink(s9, s12, **linkopts2)
        self.addLink(s10, s11, **linkopts2)
        self.addLink(s10, s13, **linkopts2)
        self.addLink(s11, s12, **linkopts2)

        # swith to host
        self.addLink(s0, h0, **linkopts1)
        self.addLink(s1, h1, **linkopts1)
        self.addLink(s2, h2, **linkopts1)
        self.addLink(s3, h3, **linkopts1)
        self.addLink(s4, h4, **linkopts1)
        self.addLink(s5, h5, **linkopts1)
        self.addLink(s6, h6, **linkopts1)
        self.addLink(s7, h7, **linkopts1)
        self.addLink(s8, h8, **linkopts1)
        self.addLink(s9, h9, **linkopts1)
        self.addLink(s10, h10, **linkopts1)
        self.addLink(s11, h11, **linkopts1)
        self.addLink(s12, h12, **linkopts1)
        self.addLink(s13, h13, **linkopts1)
        
def startNetwork():
    global net
    net = Mininet(topo=NsfnetTopo(), link=TCLink, build=False, switch=OVSKernelSwitch, autoSetMacs=True, waitConnected=True)

    remote_ip = "127.0.0.1"
    info('** Adding Floodlight Controller\n')
    net.addController('c1', controller=RemoteController, ip=remote_ip, port=6653, protocols="OpenFlow13")

    # Build the network
    net.build()
    net.start()
    net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    startNetwork()