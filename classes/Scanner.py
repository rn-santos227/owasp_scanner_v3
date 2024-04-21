from enum import Enum

class Scanner(Enum):
  OWASP_1 = "Broken Object Level Authorization"
  OWASP_2 = "Broken Authentication"
  OWASP_3 = "Broken Object Property Level Authorization"
  OWASP_4 = "Unrestricted Resource Consumption"
  OWASP_5 = "Broken Function Level Authorization"
  OWASP_6 = "Unrestricted Access to Sensitive Business Flows"
  OWASP_7 = "Server Side Request Forgery (SSRF)"
  OWASP_8 = "Security Misconfiguration"