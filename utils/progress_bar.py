from tqdm import tqdm
from concurrent.futures import as_completed

def show_progress_bar(future_tasks, total, desc="Processing", unit="item"):
  results = []

  for future in tqdm(as_completed(future_tasks), total=total, desc=desc, unit=unit):
    result = future.result()
    if result:
      results.append(result)

  return results

