from enum import Enum

class File(Enum):
  FILE_COMMANDS = "dictionaries/sql_commands_list.txt"
  FILE_ENDPOINTS = "files/endpoints.txt"
  FILE_ERRORS = "dictionaries/sql_error_messages.txt"
  FILE_HEADERS = "dictionaries/unsecure_headers.txt"
  FILE_IDS = "dictionaries/test_ids.txt"
  FILE_KEYS = "dictionaries/sensitive_keys.txt"
  FILE_KEYWORDS = "dictionaries/user_keywords.txt"
  FILE_PASSWORDS = "dictionaries/passwords.txt"
  FILE_PAYLOADS = "dictionaries/ssrf_payloads.txt"
  FILE_QUERIES = "dictionaries/queries.txt"
  FILE_TOKENS = "files/auth_tokens.txt"
  FILE_URLS = "files/usernames.txt"
  FILE_USERNAMES = "dictionaries/ssrf_test_urls.txt"
  FILE_WHITELIST = "dictionaries/whitelist_endpoints.txt"