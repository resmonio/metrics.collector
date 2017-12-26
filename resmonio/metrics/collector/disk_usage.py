from psutil import disk_usage
from resmonio.metrics.metric_utils import to_dict


def get_disk_metrics():
    # TODO: Unix only
    result = to_dict(disk_usage("/"))
    return result
