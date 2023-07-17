import streamlit as st
import matplotlib.pyplot as plt

fig = plt.figure

plt.plot([2010,2012,2014,2016,2018,2020,2022],[6.32,7.34,8.56,9.60,8.37,10.15,32.48])

plt.title('Gráfico TOTS3')

plt.xlabel('Date')
plt.ylabel('Value')

st.pyplot(fig)
