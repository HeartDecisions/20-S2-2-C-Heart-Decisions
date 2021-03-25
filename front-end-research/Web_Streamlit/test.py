# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:54:30 2021

@author: HZZ
"""

import streamlit as st
#import numpy as np
import pandas as pd

st.title("Heart Decision")

@st.cache
def load_data():
    df = pd.read_csv("fake_data.csv")
    return df

df = load_data()

st.table(df.head())

event_list = df["first_name"].unique()

event_type = st.sidebar.selectbox(
    "who?",
    event_list
)

county_list = df["height"].unique()

county_name = st.sidebar.selectbox(
    "height?",
    county_list
) 

part_df = df[(df["first_name"]==event_type) & (df['height']==county_name)]

st.write(f"there are {len(part_df)}data")


