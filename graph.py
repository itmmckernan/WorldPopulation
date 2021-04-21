import plotly.express as px
import numpy as np
import pandas as pd


data = pd.read_pickle('outputsmoothed5.pkl')

figure = px.choropleth(data,
                       locations='alpha',
                       color='birth rate',
                       animation_frame='year',
                       hover_name='country name',
                       range_color=[1, 9],
                       title='Fertility rate per country. 1955-2020 Historical Data, 2021-2100 UN Projection')
figure.show()
with open('index.html','w') as file:
    file.write(figure.to_html())