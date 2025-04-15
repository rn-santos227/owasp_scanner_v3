class Endpoint:
  def __init__(
    self,
    url: str,
    headers: dict = None,         
  ):
    self.url = url
    self.method = method.upper()