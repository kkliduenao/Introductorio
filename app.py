import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.header("Hello!")
st.write("Bienvenidas<3")
image = Image.open('cheers.jpg')

st.image(image, caption ='Brindemos')


texto = st.text_input('Escribe algo bonito', 'aquí')
st.write('Wow!! que frase más bonita es...', texto)

st.subheader("Aquí nos dedicaremos al arte")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Aquí amamos el cine")
  st.write("¿A ti te gusta?")
  resp = st.checkbox("Lo amo")
  if resp:
    st.write('Nosotras más <3')

with col2:
  st.subheader("Acá amamos el baile")
  modo = st.radio("¿A ti que te gusta bailar?", ('Salsa', 'Urbano', 'Contemporaneo'))
  if modo == 'Salsa':
    st.write("A nosotras también!!")
  if modo == 'Urbano':
    st.write('Brutal, que estilo')
  if modo == 'Contemporaneo':
    st.write('Eres genial')
  
