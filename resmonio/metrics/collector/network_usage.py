from psutil import net_io_counters
from resmonio.metrics.metric_utils import to_dict


def get_network_metrics():
    return to_dict(net_io_counters(pernic=True))
