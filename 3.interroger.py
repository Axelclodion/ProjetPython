
import streamlit as st
import pandas as pd
import sqlite3

Connexion à la base de données SQLite
conn = sqlite3.connect('example.db')

Exécution d'une requête SQL pour récupérer les données de la table 'products'
df = pd.read_sql_query("SELECT * FROM products", conn)

Affichage des données sous forme de graphique
st.line_chart(df)

Affichage des données sous forme de tableau
st.write(df)

Fermeture de la connexion
conn.close()
