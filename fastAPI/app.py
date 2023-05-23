import streamlit as st
import numpy as np
import joblib
from joblib import load


st.set_page_config(page_title="Prédiction du prix des  cryptomonaies", 
                   page_icon=":bar_chart:",
                   layout="wide")


st.title("Prédiction du prix des cryptomonaies")


st.markdown("Cette application utilise un modèle deep learning pour prédire le prix d'une cryptomonaie")

# chargement du modele

model_bnb = load("model_bnbs_lstm.joblib")
model_btc = load("model_btc_lstm.joblib")
model_eth = load("model_eth_lstm.joblib")
model_tet = load("model_tet_lstm.joblib")
model_usdc = load("model_usdc_lstm.joblib")


# chargement de la fonction pour normaliser

scaler_bnb = load("scaler_bnbs.joblib")
scaler_btc = load("scaler_btc.joblib")
scaler_eth = load("scaler_eth.joblib")
scaler_tet = load("scaler_tet.joblib")
scaler_usdc = load("scaler_usdc.joblib")

# chargement des fonctions pour labeliser


# definition d une fonction d'inference

def inference(nb_room, nb_parlour, nb_toilet, nb_kitchen, publish_type, parking, garden, is_meuble, is_moderne, neighbor, category, city):
    if publish_type == 'louer':
        vendre_ou_louer = 0
    else:
        vendre_ou_louer =  1
    
   # cat = categor.transform([category])[0]

    try:
        neigh = 0
    except:
        neigh = 0

    #ci = cit.transform([city])[0]
    
    
    new_data = np.array([
      #  nb_room, nb_parlour, nb_toilet, nb_kitchen, vendre_ou_louer, parking, garden, is_meuble, is_moderne, neigh, cat, ci
    ])
   # pred = model.predict(scaler.transform(new_data.reshape(1, -1)))

   # return pred


# l'utilisateur saisie une valeur pour chaque caracteristique de la maison


category = st.selectbox(
    'Selèctionnez la cryptomonaie :',
    ('BTC', 'BNB', 'ETH', 'TETH', 'USDC'))


# creation du bouton predict aui retourne la prediction du modele

if st.button("prédire"):

    prediction = inference(
       category)
    
    resultat = "le prix (en FCFA) de ce bien immobilier est égal à: " + str(prediction[0])

    st.success(resultat)



st.markdown('--------------------------------')


st.subheader("Application realisée par TATCHUM Ulrich")






