import unittest
from resmonio.metrics.collector.network_usage import get_network_metrics


class NetworkUsageTest(unittest.TestCase):

    def test_network(self):
        print("")
        print("Testing network usage:")
        network_usages = get_network_metrics()
        print(type(network_usages))
        print(network_usages)
