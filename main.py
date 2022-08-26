
import json

def convert_string_points_to_float(points:list):
    try:
        points = [float(point) for point in points]
    except ValueError:
        points = [0,0]
    return points

def format_csv_to_json(csv: str):
    with open(csv, 'r') as f:
        points = f.read()
        points = points.split('\n')
        points = [point.split(',')[:2] for point in points]
        points = points[1:]
        points = [convert_string_points_to_float(point) if point != [''] else [0,0] for point in points ]

        payload = {
            "geometry": {
                "points": points
            },
            "spatialReference": {
                "wkid": 4326
            }
        } 
        with open('payload.json', 'w') as f:
            data = json.dumps(payload, indent=2)
            f.write(data)

if __name__ == '__main__':
    csv_file = "Final.csv" # path to the csv file
    format_csv_to_json(csv_file)
