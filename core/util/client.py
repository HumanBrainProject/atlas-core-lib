import requests
import os

json_header = {'Content-Type': 'application/json'}
zip_header = {'Content-Type': 'application/zip'}
base_url = 'http://s2i-java-atlas-core.apps-dev.hbp.eu/'
# base_url = 'http://s2i-java-atlas-core.apps-dev.hbp.eu/' if os.getenv('ATLAS_CORE_ENV') else "http://s2i-java-atlas-core.apps.hbp.eu/"


def get_call(url, header=json_header):
    try:
        response = requests.get(base_url + url, headers=header)
    except requests.exceptions.RequestException as e:
        print(e)
        response = None
    if response is not None and response.status_code == 200:
        return response
    else:
        print('response', response)
        return None


def get_filename_from_header(header):
    name_index = header.index('filename')
    return header[(name_index+9):].replace("\"", "")


def download_tvb_data():
    url = base_url + '/tvb/dummy'
    response = get_call(url, zip_header)
    filename = get_filename_from_header(response.headers.get('Content-Disposition'))
    with open(filename, 'wb') as code:
        code.write(response.content)
