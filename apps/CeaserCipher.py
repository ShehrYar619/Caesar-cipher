import streamlit as st
from streamlit.proto.TextInput_pb2 import TextInput

def app():
    st.header("Encryption")

    def caesar_cipher(raw_text, key):
        if raw_text=="" and key==0 : return "Enter Text and key ! "
        if raw_text=="" : return "Enter Key !"
        if key==0 : return "Enter Key !" 
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
        cipher_text = ""

        for i in range(len(raw_text)):
            char = raw_text[i]
            idx = alphabet.find(char.upper())
            if idx == -1:
                cipher_text = cipher_text + char
            elif char.islower():
                cipher_text = cipher_text + shifted_alphabet[idx].lower()
            else:
                cipher_text = cipher_text + shifted_alphabet[idx] 

        return(cipher_text)

    plain_text = st.text_input("INPUT PLAIN TEXT:")
    shift_pat = int(st.number_input("INPUT KEY: "))
    st.write("Cipher Text = ",caesar_cipher(plain_text,shift_pat) )  

    st.markdown("##")
    st.info("    ")
    st.header("Decryption")

    plain_text2 = st.text_input("INPUT CIPHER TEXT:")
    shift_pat2 = st.number_input("ENTER KEY: ")
    shift_pat2 = int(shift_pat2)
    st.write("Cipher Text = ",caesar_cipher(plain_text2,26-shift_pat2) )
