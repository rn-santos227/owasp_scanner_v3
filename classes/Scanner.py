from enum import Enum

from modules.OWASP_api1 import check_api_1
from modules.OWASP_api2 import check_api_2
from modules.OWASP_api3 import check_api_3
from modules.OWASP_api4 import check_api_4
from modules.OWASP_api5 import check_api_5
from modules.OWASP_api6 import check_api_6
from modules.OWASP_api7 import check_api_7
from modules.OWASP_api8 import check_api_8
from modules.OWASP_api9 import check_api_9
from modules.OWASP_api10 import check_api_10

class Scanner:
  def __init__(self, id, function, scanner_name):
    self.id = id
    self.function = function
    self.scanner_name = scanner_name

class OWASP(Enum):
  OWASP_1 = Scanner(id="API1:2023", function=check_api_1, scanner_name="Broken Object Level Authorization")
  OWASP_2 = Scanner(id="API2:2023", function=check_api_2, scanner_name="Broken Authentication")
  OWASP_3 = Scanner(id="API3:2023", function=check_api_3, scanner_name="Broken Object Property Level Authorization")
  OWASP_4 = Scanner(id="API4:2023", function=check_api_4, scanner_name="Unrestricted Resource Consumption")
  OWASP_5 = Scanner(id="API5:2023", function=check_api_5, scanner_name="Broken Function Level Authorization")
  OWASP_6 = Scanner(id="API6:2023", function=check_api_6, scanner_name="Unrestricted Access to Sensitive Business Flows")
  OWASP_7 = Scanner(id="API7:2023", function=check_api_7, scanner_name="Server Side Request Forgery (SSRF)")
  OWASP_8 = Scanner(id="API8:2023", function=check_api_8, scanner_name="Security Misconfiguration")
  OWASP_9 = Scanner(id="API9:2023", function=check_api_9, scanner_name="Improper Inventory Management")
  OWASP_10 = Scanner(id="API10:2023", function=check_api_10, scanner_name="Unsafe Consumption of APIs")