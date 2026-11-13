import pandas as pd


def clean_bess_df(df):
    df = df[['Resource Name','Start Date','End Date','Fuel Type','Registered Capacity/Dispatchable Capacity','Jurisdiction']]
    df = df.rename(columns = { 
        'Resource Name' : 'gu_id',
        'Start Date' : 'start_date',
        'End Date' : 'end_date',
        'Fuel Type' : 'fuel_type',
        'Registered Capacity/Dispatchable Capacity' : 'capacity_mw', 
        'Jurisdiction' : 'jurisdiction'
        })
    df = df[df['fuel_type'] == 'MULTI_FUEL']
    return df

