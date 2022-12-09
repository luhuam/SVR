import streamlit as st
from multiapp import MultiApp
from apps import home,modelo1 # import your app modules here

app = MultiApp()

st.markdown("""
# Inteligencia de Negocios - Equipo B
""")
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Modelo SVR", modelo1.app)

# The main app
app.run()
