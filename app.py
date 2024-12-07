import numpy as np
import streamlit as st
import pickle

# Title
st.title("Bemorga dori tafsiya qilish:")

# Form inputs
# Age ni tanlash
Age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
# Gender tanlash
gender = st.number_input("Select your gender (female=0, male=1):", min_value=0, max_value=1, step=1)
# Blood Pressure tanlash
blood_pressure = st.selectbox(
    "Select your Blood Pressure level:",
    options=["Normal (0)", "Above normal (1)", "High (2)"]
)

# Blood Pressure qiymatini raqamga aylantirish
blood_pressure_value = {
    "Normal (0)": 0,
    "Above normal (1)": 1,
    "High (2)": 2
}[blood_pressure]

# na_to_k ni tanlash
na_to_k = st.number_input("Enter your na_to_k:", format="%.2f")

# Cholesterol tanlash
# Cholesterol ni tanlash
cholesterol = st.radio(
    "Select your Cholesterol level:",
    options=["Normal (0)", "High (1)"]
)

# Cholesterol qiymatini raqamga aylantirish
cholesterol_value = {
    "Normal (0)": 0,
    "High (1)": 1
}[cholesterol]



# Modelni chaqirish
with open('modelasosiy.pkl', 'rb') as file:
    decision_tree_model = pickle.load(file)

# Bashorat qilish
if st.button("Bashorat qil"):
    # Kiritilgan ma'lumotlarni massiv ko'rinishiga o'tkazish
    features = np.array([[Age, gender, blood_pressure, cholesterol, na_to_k]])

    # Kiritilgan ma'lumotlar sonini tekshirish
    if len(features[0]) >= 5:
        # Modelga kiritilgan ma'lumotlarni uzatish
        predict1 = decision_tree_model.predict(features)

        # Natijani chiqarish
        st.write("Sizga quyidagi dori to'g'ri keladi:")
        st.success(f"Bashorat: {predict1[0]}")
    else:
        st.error("Iltimos, barcha maydonlarni to'ldiring!")
