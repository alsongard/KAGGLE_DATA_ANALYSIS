import csv
import pandas as pd

csv_data = """1 | 01-01-2019 | 724 
1 | 01-01-2019 | 233 | 436 
1 | 01-01-2019 | 345 
1 | 01-01-2019 | 803 | 933 | 943 | 923 | 954 
1 | 01-01-2019 | 454 
"""

with open("test1.csv", "w") as f:
    f.write(csv_data)

csv.register_dialect("PipeDialect", delimiter="|")
with open("test1.csv") as csvfile:
    data = [row for row in csv.reader(csvfile, "PipeDialect")]
df = pd.DataFrame(data = data)
