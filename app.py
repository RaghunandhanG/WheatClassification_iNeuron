import streamlit as st
import numpy as np
import time

st.title('WheatClassification')

area = st.number_input("Enter the Area", value=None, placeholder="Type a value...")
perimeter = st.number_input('Enter the Perimeter',value = None,placeholder="Type a value...")
compactness = st.number_input('Enter the Compactness',value = None,placeholder="Type a value...")
length_of_kernel = st.number_input('Enter the Length of Kernel',value = None,placeholder="Type a value...")
width_of_kernel = st.number_input('Enter the Width of Kernel',value = None,placeholder="Type a value...")
asymmetry_coefficient = st.number_input('Enter the Asymmetry Coefficient',value = None,placeholder="Type a value...")
length_of_kernel_groove = st.number_input('Enter the Length of Kernel Groove',value = None,placeholder="Type a value...")

l = [[area,perimeter,compactness,length_of_kernel,width_of_kernel,asymmetry_coefficient,length_of_kernel_groove]]


if st.button("Predict"):
    
    
    try:


        with st.status("Predicting...", expanded=True , state = 'running') as status:
            time.sleep(2)
            status.update(label="Fetching Data...", state="running", expanded=True)
            time.sleep(1)
            status.update(label="Fetching Data...", state="complete", expanded=True)

    
            d = {1:'Kama',2:'Rosa',3:'Canadian'}
            import pickle 
            f = open('WheatClassifier.pickle','rb')
            model = pickle.load(f)

            predicted = model.predict([[area,perimeter,compactness,length_of_kernel,width_of_kernel,asymmetry_coefficient,length_of_kernel_groove]])

            st.metric(label="Category", value=d[predicted[0]])


    except:


        st.warning('Enter all the values and try again!', icon="⚠️")
        time.sleep(3)
        st.rerun()
