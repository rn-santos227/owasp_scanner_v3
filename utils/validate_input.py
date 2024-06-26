from classes.Type import Type 

def validate_input(data_type: Type = Type.STRING.value):
  while True:
    user_input = input(f"Please enter a Value [{data_type}]: ")
    try:
      if data_type == Type.INTEGER.value:
        value = int(user_input)
      
      elif data_type == Type.FLOAT.value:
        value = float(user_input)     
      
      elif data_type == Type.STRING.value:
        value = str(user_input) 
      
      elif data_type == Type.BOOLEAN.value:
        value = bool(user_input)

      elif data_type == Type.LIST.value:
        value = eval(user_input)
        if not isinstance(value, list):
          raise ValueError
        
      elif data_type == Type.DICTIONARY.value:
        value = eval(user_input)
        if not isinstance(value, dict):
          raise ValueError

      else:
        print("Invalid data type specified.")
        continue

      return value

    except ValueError:
      print(f"[NOTICE] Invalid input. Please enter a valid value of type {data_type}.")