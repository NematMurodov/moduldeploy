import numpy as np
import streamlit as st
import pickle

st.title = "Bemorga dori tafsiya qilish:"
#Yosh
Age = st.number_input("Enter your age:",min_value=0,max_value=120,step=1)
#Jins
gender = st.number_input("Select your gender famele=0 male=1: ",min_value=0,max_value=1,step=1)
#Qon bosimi
blood_pressure = st.number_input("Select your Cholesterol level :",min_value=0,max_value=2,step=1)
#Natriyni kaliyga nisbati
na_to_k = st.number_input("Enter your na_to_k: ",format="%.2f")
cholesterol=st.number_input("Enter your Cholesterol:",min_value=0,max_value=1,step=1)


#Tajribaga ega modelni chaqirish
with open('modelasosiy.pkl','rb') as file:
    decision_tree_model = pickle.load(file)

if st.button("bashorat qil"):
    #kiritilgan ma'lumotlarni massiv ko'rinishiga o'tkazish
    features = np.array([[Age,gender,blood_pressure,cholesterol,na_to_k]])

    if len(features[0]>=5):
        #modelga kiritilgan ma'lumotlarni uzatamiz
        predect1 = decision_tree_model.predict(features)

        #natijani chiqaramiz
        st.write(f"Sizga quyidagi dori to'g'ri keladi!")
        st.success(f"Bashorat: {predect1[0]}")
