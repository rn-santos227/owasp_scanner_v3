from urllib.parse import urlparse

def validate_url(url):
  parsed_url = urlparse(url)
  return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc != ''