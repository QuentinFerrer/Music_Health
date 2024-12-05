import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# Configurer la page pour un affichage large
st.set_page_config(layout="wide")

# Titre du dashboard
st.title("Importer et visualiser un CSV dans Streamlit")

# Charger un fichier CSV avec le widget file_uploader
uploaded_file = st.file_uploader("Importer un fichier CSV", type="csv")

if uploaded_file is not None:
    # Lire le fichier CSV avec Pandas
    df = pd.read_csv(uploaded_file)
    # Titre du dashboard
    st.title("Dashboard interactif avec Streamlit : Graphique en 4 dimensions")

    # Charger ou créer un DataFrame
    st.sidebar.header("Paramètres des données")

    # Affichage du DataFrame
    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    # Sélection des dimensions
    st.sidebar.header("Paramètres du graphique")
    x_axis = st.sidebar.selectbox("Sélectionner l'axe X", df.columns, index=0)
    y_axis = st.sidebar.selectbox("Sélectionner l'axe Y", df.columns, index=1)
    z_axis = st.sidebar.selectbox("Sélectionner l'axe Z", df.columns, index=2)
    color = st.sidebar.selectbox("Sélectionner la couleur", df.columns, index=3)

    # Créer un graphique interactif en 3D avec Plotly
    st.subheader("Graphique en 3D avec couleur comme 4e dimension")
    fig = px.scatter_3d(
        df,
        x=x_axis,
        y=y_axis,
        z=z_axis,
        color=color,
        #size='size',  # Optionnel, pour une 5e dimension
        title="Visualisation en 4 dimensions",
        opacity=0.7
    )

    # Afficher le graphique
    #st.set_page_config(layout="wide")

    # Afficher le graphique sur toute la largeur
    st.plotly_chart(fig, use_container_width=True)