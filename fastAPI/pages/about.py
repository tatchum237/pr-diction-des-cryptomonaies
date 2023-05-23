import streamlit as st



import pandas as pd
import numpy as np



st.set_page_config(page_title="Prédiction du prix des biens immobiliers", 
                   page_icon=":bar_chart:",
                   layout="wide")


st.title("Prédiction du prix des cryptomonaies")

st.markdown("Les cryptomonaies les plus utilisées.")


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("pages\BTC.jpg")

    with text_col:
        st.subheader("Bitcon (BTC)")
        st.write("""Un réseau de paiement novateur et une nouvelle forme d'argent.
          Bitcoin est un système expérimental de transfert et de vérification de propriété reposant sur un réseau de pair à pair sans aucune autorité centrale. L'application initiale et l'innovation principale du réseau Bitcoin c'est une monnaie numérique décentralisée dont l'unité de compte est le bitcoin.  """)
        st.markdown("[En savoir plus...](https://bitcoin.org/fr/)")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("pages\BNB.jpg")

    with text_col:
        st.subheader("Binance (BNB)")
        st.write("""
            Binanace coin Coin utilitaire permettant le bon fonctionnement de Binance """)
        st.markdown("[En savoir plus...](https://www.binance.com/en)")


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("pages\ETH.jpg")

    with text_col:
        st.subheader("Ethereum (ETH)")
        st.write("""
            Ethereum est la technologie gérée par la communauté qui alimente l'éther de crypto-monnaie (ETH) et des milliers d'applications décentralisées.""")
        st.markdown("[Read more...](https://www.binance.com/en)")


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("pages\TETH.jpg")

    with text_col:
        st.subheader("Tether (USDt)")
        st.write("""
           Le Tether USDT est un stablecoin émis par la société Tether Limited. Son objectif est de répliquer la valeur du dollar américain (USD). Si son cours reste stable et ses avantages nombreux, cette cryptomonnaie a connu son lot de polémiques depuis plusieurs années.""")
        st.markdown("[Read more...](https://tether.to/en/)")



with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("pages\ABC.jpg")

    with text_col:
        st.subheader("USDC (USDC)")
        st.write("""
            Une véritable interopérabilité financière nécessite un moyen stable de prix d'échange de valeur. La technologie du Centre pour les pièces stables adossées à des fiat apporte de la stabilité à la cryptographie. L'implémentation initiale est USDC, disponible en tant qu'Ethereum ERC-20.""")
        st.markdown("[Read more...](https://www.centre.io/usdc)")

