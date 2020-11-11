import pandas as pd
import plotly.express as px

df = pd.read_csv('data_log.csv')

fig = px.line(df, x = 'Time', y = 'Sensor1', title='Some random shit')
fig.show()