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
  OWASP_1 = Scanner(id="API01:2023", func_getter=lambda: __import__("modules.OWASP_api_01").check_api_01, name="Broken Object Level Authorization")