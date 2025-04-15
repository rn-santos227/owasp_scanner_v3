class Endpoint:
  def __init__(
    self,
    url: str,
    method: str = "GET",
    headers: dict = None,
    timeout: float = 10.0,
    verbose: bool = False,        
  ):
    self.url = url
    self.method = method.upper()
    self.headers = headers if headers else {}
    self.timeout = timeout
    self.verbose = verbose