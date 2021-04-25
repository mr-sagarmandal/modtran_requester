import os

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

if __name__ == "__main__":
    make_outputdir_if_absent()