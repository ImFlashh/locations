""" 
usage from command line:
python remove_duplicates.py path_to_infile path_to_outfile 
"""

import json


def load_data(path):
    with open(path, 'r+', encoding='utf-8') as json_file:
        parsed = json.load(json_file)
    return parsed


def save_data(outfile, clean_data):
    with open(outfile, 'w+', encoding='utf-8') as outfile:
        json.dump(clean_data, outfile, ensure_ascii=False)


def parse_feautre(feature):
    coordinates = feature['geometry']['coordinates']
    flatten_coordinates = list(itertools.chain(*coordinates))

    first, coors = flatten_coordinates[0], flatten_coordinates[1:-1]

    new_coors = []

    for element in coors:
        if element not in [first]:
            if element not in new_coors:
                new_coors.append(element)

    cleaned_coors = [[first] + new_coors + [first]]
    feature['geometry']['coordinates'] = cleaned_coors

    return feature


def remove_duplicates(json_data):

    clean_features = []

    for feature in json_data['features']:
        clean_feature = parse_feautre(feature)
        clean_features.append(clean_feature)

    clean_parsed = json_data
    clean_parsed['features'] = clean_features

    return clean_parsed


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='path to directory with data')
    parser.add_argument('outfile', help='path to directory with outfile')
    args = parser.parse_args()
    json_data = load_data(args.infile)
    cleaned_data = remove_duplicates(json_data)
    save_data(args.outfile, cleaned_data)
