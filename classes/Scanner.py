from enum import Enum

class Scanner:
  def __init__(self, scanner_id, scanner_name, function_name):
    self.scanner_id = scanner_id
    self.scanner_name = scanner_name
    self.function_name = function_name

class OWASP(Enum):
  OWASP_1 = Scanner("API1:2023", "Broken Object Level Authorization", "check_api_1")
  OWASP_2 = Scanner("API2:2023", "Broken Authentication", "check_api_2")
  OWASP_3 = Scanner("API3:2023", "Broken Object Property Level Authorization", "check_api_3")
  OWASP_4 = Scanner("API4:2023", "Unrestricted Resource Consumption", "check_api_4")
  OWASP_5 = Scanner("API5:2023", "Broken Function Level Authorization", "check_api_5")
  # OWASP_6 = "Unrestricted Access to Sensitive Business Flows"
  # OWASP_7 = "Server Side Request Forgery (SSRF)"
  # OWASP_8 = "Security Misconfiguration"
  # OWASP_9 = "Improper Inventory Management"
  # OWASP_10 = "Unsafe Consumption of APIs"