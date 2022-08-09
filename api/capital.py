from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        url_path = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_path.query)
        query_dic = dict(query_string_list)

        if "name" in query_dic:
            url = "https://restcountries.com/v3.1/capital/"
            query = query_dic["name"]

            response = requests.get(url + query_dic["name"])

            data = response.json()

            country = data[0]["name"]
            country_name = str(country["common"])
            message = f"{query} is the capital of {country_name}"
        else:
            message = "give a name"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

        return

