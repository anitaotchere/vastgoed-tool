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

        # Try to find woonopp, kamers, energielabel more generically
        woonopp = soup.find('li', {'class': 'object-header__key-facts--item__value'})
        kamers = soup.find('li', {'class': 'object-header__key-facts--item__value'})
        energielabel = soup.find('div', {'class': 'object-header__energylabel'})

        if woonopp and kamers and energielabel:
            st.subheader("Gegevens uit Funda:")
            st.write(f"**Woonoppervlakte:** {woonopp.text.strip()}")
            st.write(f"**Aantal kamers:** {kamers.text.strip()}")
            st.write(f"**Energielabel:** {energielabel.text.strip()}")
        else:
            st.error("Kan niet de juiste gegevens vinden op de Funda-pagina.")
    
    except Exception as e:
        st.error(f"Er ging iets mis bij het ophalen van de gegevens: {e}")
