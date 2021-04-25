
import json

def getFormattedData(content):
    flux_script = json.loads(content)['flux_script']
    docs_json_first_ind = flux_script.index("docs_json = ") + len("docs_json = ")
    docs_json_end_ind = flux_script.index(";", docs_json_first_ind)
    docs_json = flux_script[docs_json_first_ind + 1:docs_json_end_ind - 1]
    
    docs_json = json.loads(docs_json)
    out_data = {}
    for key in docs_json:
        data_root = docs_json[key]
        for reference in data_root["roots"]["references"]:
            if "attributes" in reference:
                if "data" in reference["attributes"]:
                    if "x" in reference["attributes"]["data"]:
                        out_data["x"] = reference["attributes"]["data"]["x"]
                    if "y" in reference["attributes"]["data"]:
                        out_data[reference["id"]] = reference["attributes"]["data"]["y"]
    return out_data