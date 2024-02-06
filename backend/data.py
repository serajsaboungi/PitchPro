"""
First need to install the 'gpxpy' library in the command line/terminal, using the command:
pip install gpxpy

or if you are using python3.xx (you can find out by typing "python --version" in the command line), use the command:
pip3 install gpxpy
"""
import gpxpy

"""
This function parses a .GPX file to extract the relevant data points: 
SessionDate (yyyy-mm-dd), Timestamp (hh-mm-ss), Latitude, and Longitude

:param gpx_file_path: Path to the GPX file to be parsed.
:return: A list of dictionaries, each containing the extracted information for each point.
"""


def parse_gpx_data(gpxFile):
    with open(gpxFile, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    dataPoints = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                dataPoints.append({
                    'SessionDate': point.time.strftime('%Y-%m-%d'),
                    'Timestamp': point.time.strftime('%H:%M:%S'),
                    'Latitude': point.latitude,
                    'Longitude': point.longitude
                })

    return dataPoints


gpx_file_path = '../sample_data/data1.gpx'  # using a relative path to the .GPX file rather than a local path
dataPoints = parse_gpx_data(gpx_file_path)
print(dataPoints)
