import streamlit as st
import secrets

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 1. Pengganti print() judul
st.title("Welcome to the PyPassword Generator!")

# 2. Pengganti input() menjadi kotak angka di web
nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, max_value=50, value=8)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, max_value=30, value=2)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, max_value=30, value=2)

# 3. Tombol aksi
if st.button("Generate Password", type="primary"):
    password = ""
    password_random = []

    for char in range(int(nr_letters)):
        password_random += secrets.choice(letters)

    for symbol in range(int(nr_symbols)):
        password_random += secrets.choice(symbols)

    for number in range(int(nr_numbers)):
        password_random += secrets.choice(numbers)

    secrets.SystemRandom().shuffle(password_random)
    for i in password_random:
        password += i

    # 4. Pengganti print() hasil (otomatis ada tombol copy di pojok kanan)
    st.write("Your password is:")
    st.code(password, language=None)