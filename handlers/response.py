import requests;

def process_response(request : requests, match_string, default_testing_length, verbose):
  response = request.text
  if match_string is not None:
    for string in match_string:
      if string in response:
         messaage = f"[+] {request.request.method} - \"{str(string)}\" detected: {request.request.url}"