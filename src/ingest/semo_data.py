
#%%
import datetime as dt
from irish_electricity_data import MarketClient
from transform.general import pydantic_to_df


with MarketClient() as client:
    data = client.semo.get_fpns(
        start_date=dt.date(2026, 11, 1),
        end_date=dt.date(2026, 11, 2),
    )

df = pydantic_to_df(data)

df_diff_start_and_end = df[(df['start_mw'] != df['end_mw']) & (df['resource_name'] == 'GU_404260')]

df_diff_start_and_end

# %%
