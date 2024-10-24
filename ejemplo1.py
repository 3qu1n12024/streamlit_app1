# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import datetime
import pandas as pd

st.title("Mi Primer Proyecto con streamlit")
st.write("Hola _como_ estas")

d = st.date_input('Fecha de cumpleaños', datetime.date(2019,7,6))
st.write('Tu cumpleaños es:', d)

option = st.selectbox('Como desearia ser contratado(a)?', ('Email','Telefono','Whatsapp', 'x'))
st.write('Usted seleccionó la opcion:', option)

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(df)