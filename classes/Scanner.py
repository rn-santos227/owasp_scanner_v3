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
  OWASP_2 = Scanner(id="API02:2023", func_getter=lambda: __import__("modules.OWASP_api_02").check_api_02, name="Broken Authentication")
  OWASP_3 = Scanner(id="API03:2023", func_getter=lambda: __import__("modules.OWASP_api_03").check_api_03, name="Broken Object Property Level Authorization")
  OWASP_4 = Scanner(id="API04:2023", func_getter=lambda: __import__("modules.OWASP_api_04").check_api_04, name="Unrestricted Resource Consumption")
  OWASP_5 = Scanner(id="API05:2023", func_getter=lambda: __import__("modules.OWASP_api_05").check_api_05, name="Broken Function Level Authorization")