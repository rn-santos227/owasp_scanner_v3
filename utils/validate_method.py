import argparse

def validate_method(value):
  methods = value.lower()
  if methods not in ['GET','POST','PUT','PATCH','DELETE']: 
    raise argparse.ArgumentTypeError(f"argument -m/--method: invalid choice: '{methods}' (choose from 'GET', 'POST', 'PATCH', 'PUT', 'DELETE')")
  return methods