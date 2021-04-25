import requests
import time
import csv_writer_utils
import formatting_utils
import utils

headers = {
    'Host' : 'modtran.spectral.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Accept' : 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip, deflate',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-CSRFToken' : 'bh9S5umFxQk4EFeYJjH7qmdQS4acxNVI',
    'X-Requested-With' : 'XMLHttpRequest',
    'Content-Length' : '725',
    'Origin' : 'http://modtran.spectral.com',
    'Connection' : 'keep-alive',
    'Referer' : 'http://modtran.spectral.com/modtran_home',
    'Cookie' : 'csrftoken=bh9S5umFxQk4EFeYJjH7qmdQS4acxNVI'
}

def getContentText(headers, payLoad):
    url = "http://modtran.spectral.com/ajaxRunModtran"
    s = requests.Session()
    content = s.post(url, data=payLoad, headers=headers)
    return content.text


def get_data_for_ranges(range_params, payLoad):
    data_for_ranges = {}
    range_params.sort(key=lambda params : params[0])
    for range in range_params:
        payLoad['specrng_min'] = range[0]
        payLoad['specrng_max'] = range[1]
        payLoad['resolution'] = range[2]
        headers["Content-Length"] = str(utils.calculate_content_length(payLoad))
        content = getContentText(headers, payLoad)        
        formatted_data = formatting_utils.getFormattedData(content)
        csv_writer_utils.write_csv(formatted_data, "{}_{}".format(range[0], range[1]))
        data_for_ranges[range[0]] = formatted_data
        time.sleep(1)
    merged_rows = csv_writer_utils.merge_all_dicts(data_for_ranges)
    csv_writer_utils.write_csv(merged_rows, 'newfile')