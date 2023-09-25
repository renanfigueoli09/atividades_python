import numpy as np
import pandas as pd


movies = pd.read_csv('movies.csv')

porcentagem = movies['Rotten Tomatoes %']

median = np.median(porcentagem)

print(f"mediana: {median} %")
