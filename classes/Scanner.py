from enum import Enum

class Scanner:
  def __init__(self, scanner_id, scanner_name, function_name):
    self.scanner_id = scanner_id
    self.scanner_name = scanner_name
    self.function_name = function_name

class OWASP(Enum):
  OWASP_1 = Scanner("API1:2023", "Broken Object Level Authorization", "check_api_1")
  OWASP_2 = Scanner("API2:2023", "Broken Authentication", "check_api_2")
  # OWASP_3 = "Broken Object Property Level Authorization"
  # OWASP_4 = "Unrestricted Resource Consumption"
  # OWASP_5 = "Broken Function Level Authorization"
  # OWASP_6 = "Unrestricted Access to Sensitive Business Flows"
  # OWASP_7 = "Server Side Request Forgery (SSRF)"
  # OWASP_8 = "Security Misconfiguration"
  # OWASP_9 = "Improper Inventory Management"
  # OWASP_10 = "Unsafe Consumption of APIs"