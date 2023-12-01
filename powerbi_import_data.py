# Import data into 



import pandas as pd

data = {
    "Month": ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Sales": [1200, 1330, 1500, 1650, 1400, 1770, 1800, 1900, 2200, 2022, 2200, 2120]
}

df = pd.DataFrame(data)
print(df)
