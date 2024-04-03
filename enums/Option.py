from enum import Enum

class Option(Enum):
  OPTION_1 = "Add New Endpoint"
  OPTION_2 = "Manage Endpoints Collection"
  OPTION_3 = "Perform Full Scan"
  OPTION_4 = "Perform Quick Scan"
  OPTION_5 = "Perform Specific Scan"
  EXIT = "Exit Program"