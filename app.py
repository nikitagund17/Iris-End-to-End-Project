# Import required packages
# command to run - python -m streamlit run app.py

import pandas as pd
import pickle
import streamlit as st
import numpy as np

# ctreate a header for browser
st.set_page_config(page_title='Iris-Project - nikitagund')

# Add a title
st.title("Iris End to End Project - Nikita Gund")

# take sepal length,sepal width,petal length,petal width
sep_len=st.number_input('Sepal Length : ',min_value=0.00,step=0.01)
sep_wid=st.number_input('Sepal Width : ',min_value=0.00,step=0.01)
pet_len=st.number_input('Petal Length : ',min_value=0.00,step=0.01)
pet_wid=st.number_input('Petal Width : ',min_value=0.00,step=0.01)

# Add a button to predict species
submit=st.button('Predict')

# write a function to predict species along with probability
def predict_species(pre_path,model_path):
    # Get the inputs in dataframe format
    xnew=pd.DataFrame([sep_len,sep_wid,pet_len,pet_wid]).T
    xnew.columns=['sepal_length','sepal_width','petal_length','petal_width']
    #load the preprocessor with pickle
    with open(pre_path,'rb') as file1:
        pre=pickle.load(file1)
    # Transform xnew
    xnew_pre=pre.transform(xnew)

    #Load the model with pickle
    with open (model_path,'rb') as file2:
        model=pickle.load(file2)

    # Get the predictions
    preds=model.predict(xnew_pre)

    #Get the probability of predictions
    probs=model.predict_proba(xnew_pre)

    #Get maximum probability
    max_prob=np.max(probs)

    return preds,max_prob

# Subheader to show result
st.subheader('Results are : ')

# Predicting result on the web app after submit button is pressed
if submit:
    #Get pre path and model path
    pre_path='notebook/preprocessor.pkl'
    model_path='notebook/model.pkl'

    # Get the predictions along with probability
    pred,max_prob=predict_species(pre_path,model_path)
    #Print the result
    st.subheader(f'Predicted Species is : ,{pred}')
    st.subheader(f'Probability of predictions : {max_prob:.4f}')
    #Show probability in progress bar
    st.progress(max_prob)


    

