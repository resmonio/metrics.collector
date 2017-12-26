from psutil import virtual_memory, swap_memory
from resmonio.metrics.metric_utils import to_dict


def get_virtual_memory_metrics():
    return to_dict(virtual_memory())


def get_swap_memory_metrics():
    return to_dict(swap_memory())