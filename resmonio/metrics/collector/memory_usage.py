from psutil import virtual_memory, swap_memory


def get_virtual_memory_metrics():
    return virtual_memory()


def get_swap_memory_metrics():
    return swap_memory()