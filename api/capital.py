
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# create a function that handles a query
# server should handle a Get request with a given capital name that responds with a string


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_path.query)
        dictionary = dict(query_string_list)

        if "name" in dictionary:
            url = "https://restcountries.com/v3.1/capital/"
            query = dictionary["name"]

            response = requests.get(url + dictionary["name"])

            data = response.json()

            country_name = data[0]["name"]
            answer = str(country_name["common"])
            results = f"{query} is the capital of {answer}"

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(results.encode())

        return
