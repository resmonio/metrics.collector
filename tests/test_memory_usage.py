import unittest
from resmonio.metrics.collector.memory_usage import get_virtual_memory_metrics, get_swap_memory_metrics


class DiskUsageTest(unittest.TestCase):

    def test_virtual_memory(self):
        print("Testing virtual memory usage:")
        virtual_memory_usage = get_virtual_memory_metrics()
        print(type(virtual_memory_usage))
        print(virtual_memory_usage)

    def test_swap_memory(self):
        print("Testing swap memory usage:")
        swap_memory_usage = get_swap_memory_metrics()
        print(type(swap_memory_usage))
        print(swap_memory_usage)