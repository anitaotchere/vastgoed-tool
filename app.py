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

        woonopp = soup.find(string="Wonen").find_next().text.strip()
        kamers = soup.find(string="Aantal kamers").find_next().text.strip()
        energielabel = soup.find(string="Energielabel").find_next().text.strip()

        st.subheader("Gegevens uit Funda:")
        st.write(f"**Woonoppervlakte:** {woonopp}")
        st.write(f"**Aantal kamers:** {kamers}")
        st.write(f"**Energielabel:** {energielabel}")

    except Exception as e:
        st.error(f"Er ging iets mis bij het ophalen van de gegevens: {e}")
