import streamlit as st

import plotly_express as px

from datetime import datetime

import pandas as pd
import numpy as np


st.set_page_config(page_title="Prédiction du prix des biens immobiliers", 
                   page_icon=":bar_chart:",
                   layout="wide")



BNB = pd.read_csv('pages\BNB-USD.csv')
BTC = pd.read_csv('pages\BTC-USD.csv')
ETH = pd.read_csv('pages\ETH-USD.csv')
TETH = pd.read_csv('pages\ABC.csv')
USDC = pd.read_csv('pages\BCA.csv')


st.sidebar.header("Filtrer ici")


#date = st.sidebar.date_input("Sélectionnez une date:")
price = st.sidebar.number_input("Un nombre", 0, 10000000)

#st.subheader(f"Date: {date}")



bnb_ = BNB.query(
    "Close <= @price"
)
btc_ = BTC.query(
    "Close <= @price "
)
eth_ = ETH.query(
     "Close <= @price "
)
teth_ = TETH.query(
    "Close <= @price "
)
usdc_ = USDC.query(
    "Close <= @price "
)


st.title(":bar_chart: Sales Dashboard")

st.markdown("##")

total_bnb = float(bnb_["Close"].sum())
total_eth = float(eth_["Close"].sum())
total_teth = float(teth_["Close"].sum())
total_usdc = float(usdc_["Close"].sum())
total_btc = float(btc_["Close"].sum())

mean_bnb = round(bnb_["Close"].mean(),2)
mean_eth = round(eth_["Close"].mean(), 2)
mean_teth = float(teth_["Close"].mean())
mean_btc = float(btc_["Close"].mean())
mean_usdc = float(usdc_["Close"].mean())

total = total_bnb + total_eth + total_teth + total_usdc + total_btc

mean = mean_bnb + mean_eth + mean_teth + mean_btc + mean_usdc

left_column, right_column = st.columns(2)



st.subheader("Total des closes")
st.subheader(f" {total:,}")
    


#with right_column:
  #  st.subheader("Moyenne des closes")
  #  st.subheader(f" {mean_eth:,}")


st.markdown("---")




left_column, right_column = st.columns(2)

with left_column:
     st.subheader("BTC")
     st.dataframe(btc_)
     st.subheader(f"Total close: {total_btc:,}")

with right_column:
     st.subheader("BNB")
     st.dataframe(bnb_)
     st.subheader(f"Total close: {total_bnb:,}")

left_column, right_column = st.columns(2)

with left_column:
     st.subheader("ETH")
     st.dataframe(eth_)
     st.subheader(f"Total close: {total_eth:,}")

with right_column:
     st.subheader("TETH")
     st.dataframe(teth_)
     st.subheader(f"Total close: {total_teth:,}")

st.subheader("TETH")
st.dataframe(usdc_)
st.subheader(f"Total close: {total_usdc:,}")






# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

























