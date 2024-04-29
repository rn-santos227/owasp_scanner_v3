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
  DICTIONARY_1 = "Add New Text in Dictionary"
  DICTIONARY_2 = "Read Text List in Dictionary"
  DICTIONARY_3 = "Update Text List in Dictionary"
  DICTIONARY_4 = "Remove Text in Dictionary"
  ENDPOINT_1 = "Create Endpoint"
  ENDPOINT_2 = "Read Endpoint"
  ENDPOINT_3 = "Update Endpoint"
  ENDPOINT_4 = "Delete Endpoint"
  CONFIG_1 = "Adjust Request Count"
  CONFIG_2 = "Adjust Size Threshold"
  CONFIG_3 = "Adjust Time Threshold"
  CONFIG_4 = "Adjust Rate Limit"
  CONFIG_5 = "Change Proxy URLs"
  EXIT = "Exit Program"