import pandas as pd
import re

text = "contact fbshgu2m3h4h@gmail.com or 124366464z@outlook.com"
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)
print(emails)
