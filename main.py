
import json
from pprint import pprint as pp




def format_json(csv: str):
    with open(csv, 'r') as f:
        points = f.read()
        points = points.split('\n')
        points = [point.split(',')[:2] for point in points]
        points = points[1:]
        points = [point for point in points if point != ['']]

        payload = {
            "geometry": {
                "points": points
            },
            "spatialReference": {
                "wkid": 4326
            }
        }
        with open('payload.json', 'w') as f:
            data = json.dumps(payload)
            f.write(data)

if __name__ == '__main__':
    csv_file = "path_to_csv_file" # path to the csv file
    format_json(csv_file)
