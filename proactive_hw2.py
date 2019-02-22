#!/usr/bin/env python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo

class HW2Topo(Topo):
    def build(self):
        switch = self.addSwitch('s1')
        for h in range(3):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def aggNet():
    net = Mininet(topo=HW2Topo(), controller=RemoteController(name='c0', ip='127.0.0.1', port=6633))

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    aggNet()