import pandas as pd

# učitaj Excel fajl
df = pd.read_excel("ISPY2-Imaging_Cohort_1_Clinical_Data.xlsx")

# prikaži prvih 5 redova
df.head()