__author__ = 'pkim'

import json
import argparse
import xml.etree.ElementTree as Et

def main():

    parser = argparse.ArgumentParser(description='Get file paths for input/output')
    parser.add_argument('--in', dest='input_file', required=True)
    parser.add_argument('--out', dest='output_file')
    args = parser.parse_args()

    input_file = args.input_file
    if not args.output_file:
        output_file = input_file[:input_file.rfind('.')] + ".json"

    # convert XML to json
    with open(output_file, 'a') as f:
        # parse input XML file
        for event, elem in Et.iterparse(input_file):
            if elem.tag == "row" and '_uuid' in elem.attrib:
                this_dict = dict()
                # Add _address
                this_dict['source_uri'] = elem.attrib['_address']
                for child in elem.findall('*'):
                    if child.tag == "location_1":
                        if 'latitude' in child.attrib:
                            this_dict['latitude'] = child.attrib['latitude']
                        if 'longitude' in child.attrib:
                            this_dict['longitude'] = child.attrib['longitude']
                    else:
                        this_dict[child.tag] = child.text

                # Write record to file as JSON
                json.dump(this_dict, f)
                print('', file=f)

                # this helps reduce mem usage but more can be done (see http://effbot.org/zone/element-iterparse.htm)
                elem.clear()

if __name__ == '__main__':
    main()
