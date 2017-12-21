from psutil import disk_usage


def get_disk_metrics():
    # TODO: Unix only
    return disk_usage("/")
