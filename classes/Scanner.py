from enum import Enum

from modules.OWASP_api1 import check_api_1
from modules.OWASP_api2 import check_api_2

class Scanner:
  def __init__(self, scanner_id, function, scanner_name):
    self.scanner_id = scanner_id
    self.function = function
    self.scanner_name = scanner_name

class OWASP(Enum):
  OWASP_1 = Scanner(scanner_id="API1:2023", function=check_api_1, scanner_name="Broken Object Level Authorization")
  OWASP_2 = Scanner(scanner_id="API2:2023", function=check_api_2, scanner_name="Broken Authentication")
  OWASP_3 = Scanner("API3:2023", "Broken Object Property Level Authorization")
  OWASP_4 = Scanner("API4:2023", "Unrestricted Resource Consumption")
  OWASP_5 = Scanner("API5:2023", "Broken Function Level Authorization")
  OWASP_6 = Scanner("API6:2023", "Unrestricted Access to Sensitive Business Flows")
  OWASP_7 = Scanner("API7:2023", "Server Side Request Forgery (SSRF)")
  OWASP_8 = Scanner("API8:2023", "Security Misconfiguration")
  OWASP_9 = Scanner("API9:2023", "Improper Inventory Management")
  OWASP_10 = Scanner("API10:2023", "Unsafe Consumption of APIs")