import streamlit as st
from multiapp import MultiApp
from PIL import Image
from apps import CeaserCipher,Home
app = MultiApp()


app.add_app("Home",Home.app)
app.add_app("Ceaser Cipher", CeaserCipher.app)

app.run()


