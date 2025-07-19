import logging
import requests

logger = logging.getLogger(__name__)

def handle_response(response: requests.Response, match_strings, default_length: int, verbose: bool):
  text = response.text
  method = response.request.method
  url = response.request.url

  if match_strings:
    for string in match_strings:
      if string in text:
        logger.info(f"{method} - \"{string}\" detected: {url}")

  if len(text) != default_length:
    logger.info(f"{method} - Different response length: {len(text)} - {url}")

  if verbose:
    logger.debug(f"{method} {len(text)} {url}")
         