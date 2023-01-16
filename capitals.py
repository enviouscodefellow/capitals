import json
from urllib.parse import parse_qsl, urlsplit
from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        query_string = dict(parse_qsl(urlsplit(s).query))

        if "country" in query_string:
            url = f"https://restcountries.com/v3.1/name/{query_string['country']}"
            r = requests.get(url)
            data = json.loads(r.text)
            message = f'The capital of {query_string["country"].title()} is {data[0]["capital"]}'

        elif "capital" in query_string:
            url = f"https://restcountries.com/v3.1/capital/{query_string['capital']}"
            r = requests.get(url)
            data = json.loads(r.text)
            message = f'{query_string["capital"].title()} is the capital of {data[0]["name"]["common"]}'

        else:
            message = "Please input a country or capitol city name."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return