import json


def filter_location(path, condition, newfile):
    with open(path, 'r') as handle:
        parsed = json.load(handle)
        features = parsed['features']
        filtered = [_ for _ in features if _['id'] == condition]
        with open(newfile, 'w+') as outfile:
            json.dump(filtered, outfile)
