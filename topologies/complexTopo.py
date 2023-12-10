from mininet.topo import Topo

class ComplexTopo(Topo):
    def build(self):
        #hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')
        h17 = self.addHost('h17')

        #switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')
        s16 = self.addSwitch('s16')
        s17 = self.addSwitch('s17')
        s18 = self.addSwitch('s18')
        s19 = self.addSwitch('s19')
        s20 = self.addSwitch('s20')
        s21 = self.addSwitch('s21')
        s22 = self.addSwitch('s22')

        #Links
        linkopts1 = dict(bw=100, delay='1ms', loss=1, max_queue_size=1000, use_htb=True) # between switch and host
        linkopts2 = dict(bw=1000, delay='1ms', loss=1, use_htb=True) # between 2 switches

        # swith to switch
        # first path
        self.addLink(s1, s2, **linkopts2)
        self.addLink(s2, s3, **linkopts2)
        self.addLink(s3, s4, **linkopts2)
        self.addLink(s4, s5, **linkopts2)
        self.addLink(s5, s6, **linkopts2)
        self.addLink(s6, s7, **linkopts2)
        self.addLink(s7, s8, **linkopts2)

        # second path
        self.addLink(s1, s9, **linkopts2)
        self.addLink(s9, s10, **linkopts2)
        self.addLink(s10, s11, **linkopts2)
        self.addLink(s11, s12, **linkopts2)
        self.addLink(s12, s13, **linkopts2)
        self.addLink(s13, s14, **linkopts2)
        self.addLink(s14, s15, **linkopts2)
        self.addLink(s15, s16, **linkopts2)
        self.addLink(s16, s17, **linkopts2)
        self.addLink(s17, s18, **linkopts2)
        self.addLink(s18, s19, **linkopts2)
        self.addLink(s19, s20, **linkopts2)
        self.addLink(s20, s21, **linkopts2)  
        self.addLink(s21, s22, **linkopts2)

        self.addLink(s2, s9, **linkopts2)

        # swith to host / First Path
        self.addLink(s1, h1, **linkopts1)
        self.addLink(s3, h2, **linkopts1)
        self.addLink(s3, h3, **linkopts1)
        self.addLink(s5, h4, **linkopts1)
        self.addLink(s5, h5, **linkopts1)
        self.addLink(s7, h6, **linkopts1)
        self.addLink(s7, h7, **linkopts1)
        self.addLink(s8, h8, **linkopts1)
        self.addLink(s8, h9, **linkopts1)

        # swith to host / Second Path
        self.addLink(s17, h10, **linkopts1)
        self.addLink(s17, h11, **linkopts1)
        self.addLink(s19, h12, **linkopts1)
        self.addLink(s19, h13, **linkopts1)
        self.addLink(s21, h14, **linkopts1)
        self.addLink(s21, h15, **linkopts1)
        self.addLink(s22, h16, **linkopts1)
        self.addLink(s22, h17, **linkopts1)

topos = {'complexTopo' : (lambda: ComplexTopo())}

"""
sudo mn --custom topologies/complexTopo.py --topo complexTopo --controller=remote,ip=127.0.0.1,port=6653 --switch ovsk,protocols=OpenFlow13
"""


