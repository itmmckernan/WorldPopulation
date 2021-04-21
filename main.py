import numpy as np
import pandas as pd
from tqdm import tqdm

data = pd.read_csv('fertility_un.csv')
names = pd.read_csv('countryNames.csv')
yearLabels = ["1950-1955", "1955-1960", "1960-1965", "1965-1970", "1970-1975", "1975-1980", "1980-1985", "1985-1990",
              "1990-1995", "1995-2000", "2000-2005", "2005-2010", "2010-2015", "2015-2020", "2020-2025", "2025-2030",
              "2030-2035", "2035-2040", "2040-2045", "2045-2050", "2050-2055", "2055-2060", "2060-2065", "2065-2070",
              "2070-2075", "2075-2080", "2080-2085", "2085-2090", "2090-2095", "2095-2100"]
years = [1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040,
         2045, 2050, 2055, 2060, 2065, 2070, 2075, 2080, 2085, 2090, 2095, 2100]

smoothing_level = 5

output = pd.DataFrame()
with tqdm(total=data.shape[0]) as pbar:
    for index, row in data.iterrows():
        pbar.update(1)
        for i, label in enumerate(yearLabels[:-1]):
            subyears = np.arange(years[i], years[i + 1], (years[i + 1] - years[i]) / smoothing_level)
            name = names.query('Numeric == {}'.format(row['Country code'])).to_numpy()[0][0]
            for index2, interp in enumerate(np.interp(subyears, [years[i], years[i+1]], [row[label], row[yearLabels[i+1]]])):
                output = output.append({
                    'country name': row['Name'],
                    'country code': row['Country code'],
                    'year': subyears[index2],
                    'birth rate': interp,
                    'alpha': name
                }, ignore_index=True)
print(output)
output.to_pickle('outputsmoothed5.pkl')