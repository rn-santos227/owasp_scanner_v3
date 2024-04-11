from enum import Enum

class Option(Enum):
  OPTION_1 = "Manage Endpoints Collection"
  OPTION_2 = "Perform Full Scan"
  OPTION_3 = "Perform Quick Scan"
  OPTION_4 = "Perform Specific Scan"
  OPTION_5 = "Check Bruteforce Dictionary"
  OPTION_6 = "Check Sensitive Data Bank"
  OPTION_7 = "Adjust Program Settings"
  OPTION_8 = "Open Instruction Manual"
  ENDPOINT_1 = "Create Endpoint"
  ENDPOINT_2 = "Read Endpoint"
  ENDPOINT_3 = "Update Endpoint"
  ENDPOINT_4 = "Delete Endpoint"
  CONFIG_1 = "Request Count"
  CONFIG_2 = "Size Threshold"
  CONFIG_3 = "Time Threshold"
  CONFIG_4 = "Rate Limit"
  CONFIG_5 = "Change Proxies"
  EXIT = "Exit Program"