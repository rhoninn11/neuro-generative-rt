import json
def obj2json2bytes(obj, verbose=False):
    json_txt = None
    try:
        json_txt = json.dumps(obj)
    except:
        print(f"{obj} is not JSON serializable")
    data_len = len(json_txt)
    if verbose:
        print(f" +++o2j2d-verb: {json_txt} {data_len}")
    obj_bytes = bytes(json_txt, 'utf-8')
    return obj_bytes

def bytes2json2obj(data):
    json_text = data.decode("utf-8")
    json_text = json_text.rstrip('\0')
    data = {}
    try:
        data = json.loads(json_text)
    except:
        print("był błąd")
    return data