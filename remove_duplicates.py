import json


def load_data(path):
    with open(path, 'r+', encoding='utf-8') as json_file:
        parsed = json.load(json_file)
    return parsed


def save_data(outfile, clean_parsed):
    with open(outfile, 'w+', encoding='utf-8') as outfile:
        json.dump(clean_parsed, outfile, ensure_ascii=False)


def parse_feautre(feature):
    coordinates = feature['geometry']['coordinates']

    coors_counter = {}
    new_coors = []

    for coor in coordinates:
        str_coor = ','.join(map(str, coor))
        if str_coor in coors_counter:
            if coors_counter[str_coor] < 2:
                new_coors.append(coor)
            coors_counter[str_coor] += 1
        else:
            coors_counter[str_coor] = 1
            new_coors.append(coor)

    feature['geometry']['coordinates'] = new_coors

    return feature


def remove_duplicates(path, outfile):
    parsed = load_data(path)

    clean_features = []

    for feature in parsed['features']:
        clean_feature = parse_feautre(feature)
        clean_features.append(clean_feature)

    clean_parsed = parsed
    clean_parsed['features'] = clean_features

    save_data(outfile, clean_parsed)


remove_duplicates('/home/adrian/Pobrane/admin_level_8.json',
                  '/home/adrian/Dokumenty/admin_level_8.json')
