import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.header("Hello!")
st.write("Bienvenidas<3")
image = Image.open('imagen.png')

st.image(image, caption ='Ralsei')


texto = st.text_input('hola', 'chao')
st.write('El texto escrito es', texto)

st.subheader("ahora usemos dos columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("oh, me falta el aire")
  resp = st.checkbox("y el corazón tucun tucun tucun")
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Cual es tu starter favorito?", ('Charmander', 'Squirtle', 'Bulbasaur'))
  if modo == 'Charmander':
    st.write("La opción correcta")
  if modo == 'Squirtle':
    st.write('vamo a calmarno')
  if modo == 'Bulbasaur':
    st.write('El desechable')
  
