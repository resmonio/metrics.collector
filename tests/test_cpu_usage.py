import unittest
from resmonio.metrics.collector.cpu_usage import get_cpu_count, get_cpu_metrics


class CpuUsageTest(unittest.TestCase):

    def test_cpu_count(self):
        print("")
        print("Testing CPU count : %d" % get_cpu_count())
        self.assertGreater(get_cpu_count(), 0)

    def test_cpu_percent(self):
        core_usages = get_cpu_metrics(interval=1)
        print("")
        print(type(core_usages))
        print(core_usages)
        print("Testing CPU core usages:")
        for core_usage in core_usages:
            for core_key in core_usage:
                print("%s usage : %d" % (core_key, core_usage[core_key]))



