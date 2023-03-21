import numpy as np
import pandas as pd
from markupsafe import escape
import pickle
from sklearn import svm
from flask import Flask, request, jsonify, render_template, url_for
import streamlit as st
import modulo_proyecto

# Path del modelo preentrenado
MODEL_PATH = 'models/cardio_model.pkl'

# Se recibe los datos y el modelo, devuelve la predicción
def model_prediction(x_in, model):
    x = np.asarray(x_in).reshape(1,-1)
    preds_prob = model.predict(x)
    preds = (preds_prob> 0.33).astype(int) #Modificación de umbral, usando las probabilidades - dar más fuerza al Recall
    print("Registro:", x, "Predicciones:", preds )
    return preds

def main():
    model=''
    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)    
    # Título
    html_temp = """
    <h3 style="color:#002E6F;text-align:center;">Detector de Enfermedades Cardiovasculares</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    # Lecctura de datos
    E = st.number_input("**Edad:**", min_value=1, max_value= 150, value = 50)
    G = modulo_proyecto.sexof_m(st.selectbox(label='**Sexo**', options=('Masculino', 'Femenino'))) #1 por hombre y 2 por mujer
    H = st.number_input("**Altura(cm):**", min_value=1, max_value= 300, value = 170) #en cm
    W = st.number_input("**Peso(kg):**", min_value=1.0, max_value = 400.0, value = 80.0) #en kg
    HI = st.number_input("**presión sistólica** (primero número):", min_value=70, max_value=200, value = 120)
    LO = st.number_input("**Presión diastólica** (segundo número):", min_value=40, max_value = 100, value = 80)
    optiones_bin = ["Si", "No"]
    opciones_tres = ["Normal", "Por encima de lo normal", "Muy encima de lo normal"]
    C = modulo_proyecto.opciones(st.selectbox(label="**Colesterol** según su último estudio de sangre", options=opciones_tres))
    Glu = modulo_proyecto.opciones(st.selectbox(label="**Glucosa**:", options=opciones_tres))
    F = modulo_proyecto.si_no(st.selectbox(label="**¿Usted fuma?:**", options=optiones_bin))
    BA = modulo_proyecto.si_no(st.selectbox(label="**¿Bebe alcohol?:**", options=optiones_bin))
    A = modulo_proyecto.si_no(st.selectbox(label="**¿Es una persona activa?:**", options=optiones_bin))
    IMC = round((W)/((H**2))*10000, 1)


    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Respuesta:"): 
        x_in =[np.float_(G),
                    np.float_(H),
                    np.float_(W),
                    np.float_(HI),
                    np.float_(LO),
                    np.float_(C),
                    np.float_(Glu),
                    np.float_(F),
                    np.float_(BA),
                    np.float_(A),
                    np.int(E),
                    np.float_(IMC),
                    ]



        predictS = modulo_proyecto.resultados_finales(model_prediction(x_in, model))
        st.success('Resultados: {}'.format(predictS))

if __name__ == '__main__':
    main()

#registro_data = registro_data['id', 'Edad', 'Sexo', 'Altura', 'Peso','Presion_sis', 'Presion_dia', 'Colesterol', 'Glucosa', 'Fuma', 'Alcohol', 'Actividad','Prediccion'] 
            #almacenar en un dataset los datos que se cargan --> proximo paso 