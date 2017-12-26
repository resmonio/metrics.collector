from psutil import cpu_percent, cpu_count


def get_cpu_count():
    return cpu_count()


def get_cpu_metrics(interval):
    result = cpu_percent(interval=interval, percpu=True)
    result = [{"core_%d" % index: core_usage} for index, core_usage in enumerate(result)]
    return result
