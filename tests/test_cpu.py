import unittest
from psutil import cpu_count, cpu_percent


class CpuTest(unittest.TestCase):

    def test_cpu_count(self):
        print("Testing CPU count : %d" % cpu_count())
        self.assertGreater(cpu_count(), 0)

    def test_cpu_percent(self):
        core_usages = cpu_percent(interval=1, percpu=True)
        print("Testing CPU core usages:")
        for usage in core_usages:
            print("CPU core usage : %d" % usage)
            self.assertGreaterEqual(usage, 0)



