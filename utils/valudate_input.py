def validate_input(data_type = "str"):
  while True:
    user_input = input(f"Please enter a Value [{data_type}]: ")
    try:
      break
    except ValueError:
      print(f"[NOTICE] Invalid input. Please enter a valid value of type {data_type}.")