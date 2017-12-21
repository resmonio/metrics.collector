from psutil import cpu_percent, cpu_count


def get_cpu_count():
    return cpu_count()


def get_cpu_metrics(interval):
    return cpu_percent(interval=interval, percpu=True)
