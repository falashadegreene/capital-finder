
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# create a function that handles a query
# server should handle a Get request with a given country name that responds with a string

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_path.query)
        query_dictionary = dict(query_string_list)

        if "capital" in query_dictionary:
            url = "https://restcountries.com/v3.1/capital/"
            query = query_dictionary["capital"]

            response = requests.get(url + query)
            data = response.json()

            country_name = data[0]["name"]
            country = str(country_name["common"])
            message = f"The capital of {country} is {query}"

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(message.encode())

        return
