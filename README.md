# Intro
Generé un modelo de Regresión Logistica, que puse en producción usando Streamlit y Google Cloud. Este modelo predice la posibilidad de desarrollar una enfermedad cardiovascular.

##  1. Entrenamiento del modelo
Entrené varios modelos, seleccionado el de Regresión logística con un cambio de umbral. Este último cambio es util para mejorar el "recall", como es un modelo que predice salud es preferible disminuir los Falsos Negativos.

##  2. Producción en servidor local - preparación del entorno

Creamos un entorno con python 3.7, e instalamos las dependencias necesarias.

    $   conda create -n ApiCrop
    $   conda activate ApiCrop
    $   conda install python=3.7
    $   pip install -r requirements.txt
    $   streamlit run app.py
    
##  3. Producción en servidor remoto

    *   Activar una cuenta en google cloud
    *   Crear proyecto en google cloud
    *   Instalar GoogleCloudSDK
    *   Ejecutar en la terminal:
    
    $ gcloud init
    $ gcloud app deploy app.yaml --project "Nombre del proyecto"
    

## Referencias
* Producción: https://proyecto-cardio-377818.uc.r.appspot.com/
* Dataset "cardio_train.csv", Fuente: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset
* Producción de servidor local y servidor remoto: https://github.com/DavidReveloLuna/API_Gcloud_Streamlit
* Archivos Dockerfile, app.yaml, Pipfile, Fuente: https://github.com/DavidReveloLuna/API_Gcloud_Streamlit
