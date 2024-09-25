import pandas as pd

Revenue = {
    "Movies": ["Look who\'s Back","Downfall","Stalingrad"],
    "Revenue": [3000000,1000000,6000000],
    "Budget": [999999,2000000,3000000]
}

series1 = pd.DataFrame(Revenue).set_index('Movies')
modified = series1.sort_values(ascending=False, by='Revenue')
print(modified)
