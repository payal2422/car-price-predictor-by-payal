
import pandas as pd

# Sample dataset
data = {
    "Car Name": ["Maruti Alto", "Hyundai i20", "Honda City"],
    "Year": [2010, 2015, 2018],
    "Price (in Lakh)": [2.5, 4.8, 7.6]
}

df = pd.DataFrame(data)
print("Car Price Table:")
print(df)
