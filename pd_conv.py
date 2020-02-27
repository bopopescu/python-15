import pandas as pd
s = pd.read_csv("/home/tibil/Downloads/Fire_Incidents_Data.csv")
s.to_json("fire11.json")
