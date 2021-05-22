import os
import sys

def dumpContent(content):
    try:
        with open('./out/out.json', 'w+') as file:
            file.write(json.dumps(content, indent=4))
    finally:
        file.close()

def calculate_content_length(payload):
    keys = payload.keys()
    values = payload.values()    
    totalLength = len(keys) - 1 + len(keys) #ampersands in between each kv pair and = sign
    for key in keys:
        totalLength += len(str(key))
    for val in values:
        totalLength += len(str(val))
    return totalLength

def make_outputdir_if_absent():
    if not os.path.isdir('./out'):
        os.mkdir('./out')

def get_min_max_range(range_params):
    minimum = sys.maxsize
    maximum = -1
    for range in range_params:
        minimum = min(minimum, range[0])
        maximum = max(maximum, range[1])
    return [minimum, maximum]

def get_file_name(range_params):
    min_max = get_min_max_range(range_params)
    return "{}-{}".format(min_max[0], min_max[1])

def get_payload_row(payLoad):
    row = []
    for key, value in payLoad:
        if key in ("specrng_max", "specrng_min", "resolution"):
            continue
        row.append("{}-{}".format(key, value))
    return row

if __name__ == "__main__":
    make_outputdir_if_absent()