import gpxpy


def parse_gpx_data(gpx_file_path):
    """
    Parses a GPX file to extract relevant data points: SessionDate, Timestamp, Latitude, and Longitude.

    :param gpx_file_path: Path to the GPX file to be parsed.
    :return: A list of dictionaries, each containing the extracted information for each point.
    """
    with open(gpx_file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    data_points = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                data_points.append({
                    'SessionDate': point.time.strftime('%Y-%m-%d'),
                    'Timestamp': point.time.strftime('%H:%M:%S'),
                    'Latitude': point.latitude,
                    'Longitude': point.longitude
                })

    return data_points


gpx_file_path = '../sample_data/data1.gpx'
data_points = parse_gpx_data(gpx_file_path)
print(data_points)
