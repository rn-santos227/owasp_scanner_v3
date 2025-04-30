from enum import Enum

from modules.OWASP_api_01 import check_api_01
from modules.OWASP_api_02 import check_api_02
from modules.OWASP_api_03 import check_api_03
from modules.OWASP_api_04 import check_api_04
from modules.OWASP_api_05 import check_api_05
from modules.OWASP_api_06 import check_api_06
from modules.OWASP_api_07 import check_api_07
from modules.OWASP_api_08 import check_api_08
from modules.OWASP_api_09 import check_api_09
from modules.OWASP_api_10 import check_api_10

class Scanner:
  def __init__(self, id, func_getter, name):
    self.id = id
    self._func_getter = func_getter
    self.name = name

class OWASP(Enum):
  OWASP_1 = Scanner(id="API01:2023", function=check_api_01, name="Broken Object Level Authorization")
  OWASP_2 = Scanner(id="API02:2023", function=check_api_02, name="Broken Authentication")
  OWASP_3 = Scanner(id="API03:2023", function=check_api_03, name="Broken Object Property Level Authorization")
  OWASP_4 = Scanner(id="API04:2023", function=check_api_04, name="Unrestricted Resource Consumption")
  OWASP_5 = Scanner(id="API05:2023", function=check_api_05, name="Broken Function Level Authorization")
  OWASP_6 = Scanner(id="API06:2023", function=check_api_06, name="Unrestricted Access to Sensitive Business Flows")
  OWASP_7 = Scanner(id="API07:2023", function=check_api_07, name="Server Side Request Forgery (SSRF)")
  OWASP_8 = Scanner(id="API08:2023", function=check_api_08, name="Security Misconfiguration")
  OWASP_9 = Scanner(id="API09:2023", function=check_api_09, name="Improper Inventory Management")
  OWASP_10 = Scanner(id="API10:2023", function=check_api_10, name="Unsafe Consumption of APIs")