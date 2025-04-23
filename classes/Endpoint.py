from utils.validate_method import validate_method
from utils.validate_url import validate_url

import helpers.color_text as color

class Endpoint:
  def __init__(
    self,
    url: str,
    method: str = "GET",
    headers: dict = None,
    timeout: float = 10.0,
    verbose: bool = False,
    data: str = None,
    json: dict = None,
    response = None 
  ):
    self.url = url
    self.method = method.upper()
    self.headers = headers if headers else {}
    self.timeout = timeout
    self.verbose = verbose
    self.data = data
    self.json = json
    self.response = response

  def __repr__(self):
    return (
      f"Endpoint(url={self.url}, method={self.method}, headers={self.headers}, "
      f"timeout={self.timeout}, verbose={self.verbose}, data={self.data}, "
      f"json={self.json}, response={self.response})"
    )
  
  def __str__(self) -> str:
    parts = [self.url]
  
  def to_dict(self) -> dict:
    return {
      "endpoint": self.url,
      "method": self.method,
      "headers": self.headers,
      "timeout": self.timeout,
      "verbose": self.verbose,
      "data": self.data,
      "json": self.json,
      "response": self.response
    }
  
  def is_valid(self) -> bool:
    return validate_url(self.url) and validate_method(self.method)

  
  def _normalize_method(self, method):
    try:
      return validate_method(method).upper()
    
    except Exception as e:
      color.warning(f"METHOD ERROR {e}")
      return "INVALID"