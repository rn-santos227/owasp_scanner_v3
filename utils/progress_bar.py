from tqdm import tqdm
from concurrent.futures import as_completed

def show_progress_bar(future_tasks, total, desc="Processing", unit="item"):
  results = []