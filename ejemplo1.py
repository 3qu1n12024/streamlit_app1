# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import streamlit as st
import datetime
import pandas as pd

st.title("Mi Primer Proyecto con streamlit")
st.write("Hola _como_ estas")

df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.dataframe(df.head(15))
st.map(df)
