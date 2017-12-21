import unittest
from resmonio.metrics.collector.cpu_usage import get_cpu_count, get_cpu_metrics


class CpuTest(unittest.TestCase):

    def test_cpu_count(self):
        print("Testing CPU count : %d" % get_cpu_count())
        self.assertGreater(get_cpu_count(), 0)

    def test_cpu_percent(self):
        core_usages = get_cpu_metrics(interval=1)
        print(type(core_usages))
        print(core_usages)
        print("Testing CPU core usages:")
        for usage in core_usages:
            print("CPU core usage : %d" % usage)
            self.assertGreaterEqual(usage, 0)



