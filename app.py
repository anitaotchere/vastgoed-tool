import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Vastgoed Deal Checker")

funda_url = st.text_input("Plak hier de Funda-link van het pand:")

if funda_url:
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(funda_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Zoek naar het energielabel
        energielabel = soup.find('div', {'class': 'object-header__energylabel'})
        
        # Zoek naar de koopprijs
        koopprijs = soup.find('div', {'class': 'object-price'})

        # Controleer of beide gegevens zijn gevonden
        if energielabel and koopprijs:
            st.subheader("Gegevens uit Funda:")
            st.write(f"**Energielabel:** {energielabel.text.strip()}")
            st.write(f"**Koopprijs:** {koopprijs.text.strip()}")
        else:
            st.error("Kan niet de juiste gegevens vinden op de Funda-pagina.")
    
    except Exception as e:
        st.error(f"Er ging iets mis bij het ophalen van de gegevens: {e}")
