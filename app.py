import streamlit as st

def decimal_to_binary(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    return binary

st.title("Convertisseur Décimal -> Binaire")

nombre = st.number_input("Entrez un nombre décimal :", min_value=0, step=1, value=0)

if st.button("Convertir"):
    resultat = decimal_to_binary(int(nombre))
    st.success(f"Le résultat en binaire est : **{resultat}**")
