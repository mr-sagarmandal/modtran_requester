import csv
import sys 
import utils
from datetime import datetime

def merge_lists(list1, list2):
    list1.extend(list2)
    return list1

def merge_dicts(base_dict, curr_dict):
    used_keys = {'x'}
    for key in base_dict.keys():
        if key in used_keys:
            continue
        closest_key = ''
        closest_diff = sys.float_info.max
        backward = False
        for curr_key in curr_dict.keys():
            if curr_key in used_keys:
                continue
            base_last_curr_first = abs(base_dict[key][-1] - curr_dict[curr_key][0]) 
            if closest_diff > base_last_curr_first:
                closest_diff = base_last_curr_first
                closest_key = curr_key
        used_keys.add(closest_key)
        base_dict[key] = merge_lists(base_dict[key], curr_dict[closest_key])
    base_dict['x'] = merge_lists(base_dict['x'], curr_dict['x'])
    return base_dict    

def merge_all_dicts(data):
    merged_rows = {}
    for key in sorted(data.keys()):
        if len(merged_rows) == 0:
            merged_rows = data[key]
            continue
        merged_rows = merge_dicts(merged_rows, data[key])
    return merged_rows

def write_csv(content, payLoad, fileName):
    datetimeNow = datetime.utcnow().strftime('%y-%m-%d_%H-%M-%S') 
    utils.make_outputdir_if_absent()
    with open("./out/{}_{}.csv".format(fileName, datetimeNow), 'w+', newline='') as output_file:
        data_writer = csv.writer(output_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(payLoad.keys())
        data_writer.writerow(payLoad.values())
        header_row = sorted(content.keys(), reverse=True)
        data_writer.writerow(header_row)
        for i in range(0, len(content['x'])):
            row = []
            for key in sorted(content.keys(), reverse=True):
                row.append(content[key][i])
            data_writer.writerow(row)
        