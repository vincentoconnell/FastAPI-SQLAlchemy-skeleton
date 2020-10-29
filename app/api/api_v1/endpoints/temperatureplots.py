from app.core import TemperatureDAO, schemas
from app.core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi import APIRouter
from datetime import datetime
import pandas as pd
import numpy as np
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
import plotly.express as px
import plotly.graph_objects as go
from plotly.io import to_html


router = APIRouter()

# plot server-side rendering
@router.get("/plots/temp", response_class=HTMLResponse)
async def temp_plot_get(startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dftemp = TemperatureDAO.get_temp_by_date_range_as_dataframe(db, startdate, enddate, offset=offset, limit=limit)

    dfData = pd.json_normalize(dftemp['data'])
    dftemp = pd.concat([dftemp, dfData], axis=1)

    # filter empty data for a column we care about
    if "degrees" in dftemp:
        dftemp = dftemp[["name", "timestamp", "degrees"]]
        dftemp = dftemp[dftemp.degrees.notnull()]
    else:
        return "No degrees data in date range."

    fig = px.line(dftemp, x='timestamp', y='degrees', line_shape='hv', title='Temperature over time')
    fig.update_traces(line_color='#fc2403')
    fig.update_traces(name="temperature")
    fig.update_traces(showlegend = True)
    # to combine a second data set in a figure
    # fig2 = px.line(df, x='time', y='measure', title= 'desired figure title')
    # fig2.update_traces(line_color='#0390fc')
    # fig2.update_traces(name="measure2")
    # fig2.update_traces(showlegend = True)
    # fig2.add_trace(fig.data[0])
    return to_html(fig, full_html=True)


# table server-side rendering
@router.get("/tables/temp", response_class=HTMLResponse)
async def temp_table_get(startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    df = TemperatureDAO.get_temp_by_date_range_as_dataframe(db, startdate, enddate, offset=offset, limit=limit)

    dfData2 = pd.json_normalize(df['data'])
    df = pd.concat([df, dfData2], axis=1)

    # void key errors with dynamic data
    if 'temp_warning' not in df:
        df['temp_warning'] = None

    if "degrees" in df:
        dfSubset = df[["name", "timestamp", "degrees", "temp_warning"]]
        df = dfSubset[dfSubset.degrees.notnull()]
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[df.name, df.timestamp, df.degrees, df.temp_warning],
                    fill_color='lavender',
                    align='left'))
        ])

        return to_html(fig, full_html=True)

    else:
        return "No degrees data in date range."

# table server-side rendering# dynamic table created with whatever data found
@router.get("/tables/tempdynamic", response_class=HTMLResponse)
async def temp_table_super_get(startdate: datetime, enddate: datetime, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    df = TemperatureDAO.get_temp_by_date_range_as_dataframe(db, startdate, enddate, offset=offset, limit=limit)

    dfData2 = pd.json_normalize(df['data'])
    df = pd.concat([df, dfData2], axis=1)
    
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=df.transpose().values.tolist(),
                fill_color='lavender',
                align='left'))
    ])
    return to_html(fig, full_html=True)
