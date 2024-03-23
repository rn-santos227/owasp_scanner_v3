import argparse

def validate_method(value):
  method = value.lower()
  if method not in ['get','post','put','patch','delete']: 
    raise argparse.ArgumentTypeError(f"argument -m/--method: invalid choice: '{method}' (choose from 'GET', 'POST', 'PATCH', 'PUT', 'DELETE')")
  return method