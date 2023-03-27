
import streamlit as st
import pandas as pd


# Connexion à la base de données MySQL
cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='database')

# Exécution d'une requête SQL pour récupérer les données de la table 'table_name'
query = "SELECT * FROM table_name"
df = pd.read_sql(query, cnx)

# Affichage des données sous forme de graphique
st.line_chart(df)

# Affichage des données sous forme de tableau
st.write(df)
