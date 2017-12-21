import unittest
from resmonio.metrics.collector.disk_usage import get_disk_metrics


class DiskUsageTest(unittest.TestCase):

    def test_disk(self):
        print("")
        print("Testing disk usage:")
        disk_usages = get_disk_metrics()
        print(type(disk_usages))
        print(disk_usages)
