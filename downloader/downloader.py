#!/user/bin/env python3
import requests


def downloads(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as output_file:
        output_file.write(get_response.content)


downloads("")
