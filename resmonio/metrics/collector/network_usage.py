from psutil import net_io_counters


def get_network_metrics():
    return net_io_counters(pernic=True)