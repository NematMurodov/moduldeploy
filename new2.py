import pickle
import streamlit as st


st.title("Mijozlarni Qarori")

age = st.number_input("Yoshni kiriting: ", min_value=10, max_value=150, step=1)
gender = st.selectbox("Jinsini tanlang: ", ["Erkak", "Ayol"])
location = st.selectbox("Mijozni shaharini tanlang", ['Houston', 'Los Angeles', 'Miami', 'Chicago', 'New York'])
submon=st.number_input("Mijoz necha oydan beri a'zoligi",min_value=0, max_value=20,step=1)
monthly = st.number_input("Oylik hisoboti (%)", min_value=0, max_value=100)


gender_encoded = 1 if gender == "Erkak" else 0

location_mapping = {
    'Houston': 0,
    'Los Angeles': 1,
    'Miami': 2,
    'Chicago': 3,
    'New York': 4
}
location_encoded = location_mapping[location]

with open('Churn.pkl', 'rb') as file:
    churn = pickle.load(file)

if st.button("Natijani ko'rish uchun bosing!"):
    churn_result = churn.predict([[age, gender_encoded, location_encoded,submon ,monthly]])    
    if churn_result == 0:
        st.success("Sizning mijozingiz qoladi.")
    else:
        st.error("Sizning mijozingiz ketadi.")
