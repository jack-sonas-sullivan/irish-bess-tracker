
#%%
import datetime as dt
from irish_electricity_data import MarketClient

with MarketClient() as client:
    start, end = dt.datetime(2025, 1, 15, 10), dt.datetime(2025, 1, 15, 15)
    data = client.eirgrid.get_outturn_wind(start, end)
    print(data.wind_ie)
    help(client.eirgrid.get_fpns)
    

# %%
