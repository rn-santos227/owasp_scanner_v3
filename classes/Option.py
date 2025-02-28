from enum import Enum

class Option(Enum):
  OPTION_1 = "Manage Endpoints Collection"
  OPTION_2 = "Perform Full Scan"
  OPTION_3 = "Perform Quick Scan"
  OPTION_4 = "Perform Specific Scan"
  OPTION_5 = "Check Brute-Force Dictionary"
  OPTION_6 = "Check Sensitive Data Bank"
  OPTION_7 = "Check Authentication Tokens"
  OPTION_8 = "Adjust Program Settings"
  OPTION_9 = "Open Instruction Manual"
  DATA_1 = "Show Sensitive Data Count"
  DATA_2 = "Search Sensitive Data in List"
  DATA_3 = "Add New Sensitive Data to List"
  DATA_4 = "Delete a Sensitive Data from List"
  DICTIONARY_1 = "Show Dictionary Text Count"
  DICTIONARY_2 = "Search Dictionary Text"
  DICTIONARY_3 = "Add Text in Dictionary"
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
  TOKEN_1 = "View Auth Tokens"
  TOKEN_2 = "Save Auth Token"
  TOKEN_3 = "Remove Auth Token"
  EXIT = "Exit Program"