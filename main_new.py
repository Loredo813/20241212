from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.link import TCLink
from mininet.cli import CLI
import time
import threading
from normal_ping import normal_flow
from abnormal_ping import abnormal_flow
from plot_rtt import plot_rtt_results
from statsic import calculate_rtt_statistics


class BandwidthDelayTopo(Topo):
    def build(self):
        # Create hosts and servers
        h1 = self.addHost('h1', ip='140.115.154.245/24')        # Host1
        s1 = self.addHost('s1', ip='140.115.154.246/24')        # Server1
        s2 = self.addHost('s2', ip='140.115.154.247/24')        # Server2

        # Create Open vSwitch
        sw1 = self.addSwitch('sw1')                            # Switch1

        # Connect hosts and servers to the switch with specific link parameters
        self.addLink(h1, sw1, cls=TCLink, bw=10)
        self.addLink(s1, sw1, cls=TCLink, bw=10)
        self.addLink(s2, sw1, cls=TCLink, bw=10)


def run_experiment(net):
    # Get hosts and servers
    h1 = net.get('h1')
    s1 = net.get('s1')
    s2 = net.get('s2')

    normal_rtt_results = []
    abnormal_rtt_results = []

    print("Starting normal and abnormal flow experiments...")
    normal_thread = threading.Thread(target=normal_flow, args=(net, normal_rtt_results))
    abnormal_thread = threading.Thread(target=abnormal_flow, args=(net, abnormal_rtt_results))

    normal_thread.start()
    time.sleep(5)
    abnormal_thread.start()

    normal_thread.join()
    abnormal_thread.join()

    print("Calculating and plotting RTT statistics...")

    normal_stat = calculate_rtt_statistics(normal_rtt_results)
    if normal_stat:
        print("Normal_RTT Statistics:")
        print(f"  Average RTT: {normal_stat['average']} ms")
        print(f"  Minimum RTT: {normal_stat['min']} ms")
        print(f"  Maximum RTT: {normal_stat['max']} ms")
        print(f"  Standard Deviation: {normal_stat['std_deviation']} ms")

    plot_rtt_results(normal_rtt_results, title="Normal RTT Over Time")

    abnormal_stat = calculate_rtt_statistics(abnormal_rtt_results)
    if abnormal_stat:
        print("Abnormal_RTT Statistics:")
        print(f"  Average RTT: {abnormal_stat['average']} ms")
        print(f"  Minimum RTT: {abnormal_stat['min']} ms")
        print(f"  Maximum RTT: {abnormal_stat['max']} ms")
        print(f"  Standard Deviation: {abnormal_stat['std_deviation']} ms")

    plot_rtt_results(abnormal_rtt_results, title="Abnormal RTT Over Time")
    print("Experiment completed.")


def start_network():
    # Create topology and start network
    topo = BandwidthDelayTopo()
    net = Mininet(topo=topo, controller=Controller, switch=OVSSwitch, link=TCLink)
    net.start()

    print("Network started. You can use the CLI to interact with the network.")

    # Add custom command to CLI
    def run_custom_experiment():
        run_experiment(net)

    CLI.do_run_experiment = lambda self, line: run_custom_experiment()

    try:
        CLI(net)
    finally:
        print("Stopping network...")
        net.stop()


def main():
    start_network()


if __name__ == '__main__':
    main()
