from enum import Enum

class Scanner:
  def __init__(self, id, func_getter, name):
    self.id = id
    self._func_getter = func_getter
    self.name = name

  @property
  def function(self):
    return self._func_getter() 

class OWASP(Enum):
  pass