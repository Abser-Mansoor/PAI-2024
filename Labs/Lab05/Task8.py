import pandas as pd
import re

text = "come to place at 12/09/2023, or go to convention scheduled for Sep 12, 2023, and remember to arrive at 2023-09-12"
patterns = [
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',     # For 12/09/2023
        r'\b\d{4}-\d{1,2}-\d{1,2}\b',     # For 2023-09-12
        r'\b[A-Za-z]{3} \d{1,2}, \d{4}\b' # For Sep 12, 2023
]
    
dates = []
for pattern in patterns:
    dates.extend(re.findall(pattern, text))
    
print(dates)
