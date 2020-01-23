from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import CPULimitedHost

class topocls(Topo):

    def __init__(self, **opts):

        super(topocls, self).__init__(**opts)

        # Add hosts and switches
        h1 = self.addHost('Patient1',  ip='10.0.0.10')
        h2 = self.addHost('Patient2',  ip='10.0.0.12')
        h3 = self.addHost('Patient3',  ip='10.0.0.13')
        h4 = self.addHost('Patient4',  ip='10.0.0.14')

        # Adding switches
        s1 = self.addSwitch('Hospital1')
        s2 = self.addSwitch('Hospital2')
        s3 = self.addSwitch('Hospital3')
        s4 = self.addSwitch('Hospital4')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)


def run():
    c = RemoteController('oxygen', '127.0.0.1', 6633)
    net = Mininet(topo=topocls(), host=CPULimitedHost, controller=None)
    net.addController(c)
    net.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
