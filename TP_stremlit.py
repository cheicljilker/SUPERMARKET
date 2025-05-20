## STEP 1 : Libraries and initialisation
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.compose import make_column_selector as selector
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import  Ridge
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly.express as px

# STEP 2 : Streamlit configuration
st.set_page_config(page_title="SUPERMARKET_DATASET", layout="wide")
st.title("Analyse des supermarchés des USA en fonction des états")

# STEP 3 : Data loading
st.title("Step 3 - Importation de la base des données des supermarchés")
uploaded_file = st.file_uploader("Téléversez un fichier xlsx", type="xlsx")
df = pd.read_excel("supermarket_dataset.xlsx")

# STEP 4 :  Saluer l'utilisateur
name = st.text_input("Quel est votre prénom ?")
if name:
    st.write(f"Bonjour {name} 👋")

#STEP 5 : Affichage d’un premier graphique (ventes par ville)
st.title("Total des ventes par ville")
sales_by_city = df.groupby("City")["Sales"].sum().reset_index()
fig_city = px.bar(sales_by_city, x="City", y="Sales", color="City", title="Total des ventes par ville")
st.plotly_chart(fig_city)

# STEP : Corrélations
st.subheader("Corrélations entre colonnes numériques")
corr = df.select_dtypes(include='number').corr()
st.dataframe(corr)
