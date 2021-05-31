import streamlit as st
from PIL import Image

def app():
    st.header("Ceaser Cipher")
    st.markdown("A **Caesar cipher** is a simple method of encoding messages. Caesar ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. A Caesar cipher with a shift of 11 would encode an A as a B, an M as an N, and a Z as an A, and so on. The method is named after Roman leader Julius Caesar, who used it in his private correspondence.")
    image = Image.open('abc.jpeg')
    st.image(image)
    st.subheader("Using a Caesar Cipher :")
    st.markdown("**Steps for designing and using a Caesar cipher**")
    st.markdown("1. Choose a value to shift the alphabet by.")
    st.markdown("2. Make a table where the top row contains letters in standard alphabetical order, and the bottom row is the new shifted alphabet.")
    st.markdown("3. Encode the message by exchanging each letter in the message with the equivalent shifted letter.")
    st.markdown("4. Make sure that the message’s intended recipient knows the shifting scheme you used to encode the message so they can decode it.")
    st.markdown("5. To decrypt a message encoded with a Caesar cipher, simply take the value of 26 minus the shift value, and apply that new value to shift the encoded message back to its original form.")