from enum import Enum

class File(Enum):
  FILE_COMMANDS = "dictionaries/sql_commands_list.txt"
  FILE_ENDPOINTS = "files/endpoints.txt"
  FILE_ERRORS = "dictionaries/sql_error_messages.txt"
  FILE_IDS = "dictionaries/test_ids.txt"
  FILE_KEYS = "dictionaries/sensitive_keys.txt"
  FILE_KEYWORDS = "dictionaries/user_keywords.txt"
  FILE_PASSWORDS = "dictionaries/passwords.txt"
  FILE_PAYLOADS = "dictionaries/ssf_payloads.txt"
  FILE_QUERIES = "dictionaries/queries.txt"