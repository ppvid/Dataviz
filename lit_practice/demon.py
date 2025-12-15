import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

x=np.linspace(0,10,100)
y=np.sin(x)
fig,ax=plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
st.divider()

import altair as alt
data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

c=(
    alt.Chart(data)
    .mark_circle()
    .encode(
        x='a',y='b',
        size='c',
        color='c',
        tooltip=['a','b','c']
    )
)
st.altair_chart(c,use_container_width=True)

import plotly.express as px
df=px.data.iris()
fig=px.scatter(df,x='sepal_width',y='sepal_length')
st.plotly_chart(fig,key='iris',on_select='rerun')