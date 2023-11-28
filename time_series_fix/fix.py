from math import ceil


def fix(timeseries, fr, to, interval):
    result = []
    fr, to = round_up(fr),  round_up(to)
    for r in range(fr, to, interval):
        t = find_by_timestamp(timeseries, r)
        if t:
            result.append(t)
        else:
            result.append({'value': None, 'timestamp': r})

    return result


def find_by_timestamp(timeseries, timestamp):
    if len(timeseries) != 0:
        for i in timeseries:
            i['timestamp'] = round_up(i['timestamp'])
            if i['timestamp'] == timestamp:
                return i


def round_up(timestamp):
    return ceil(timestamp / 10) * 10
