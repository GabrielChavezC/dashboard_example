# Librerias ----------------------------------------

import os, sys
import argparse
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código
import platform 

sistema_operativo = platform.system()

    
# Definir extension de ejecutables ---------------------------------------- 

if sistema_operativo == 'Windows':
        extension_binarios = ".exe"
else:
        extension_binarios = ""
# Preproceso ---------------------------------------- 
#os.system(f"python{extension_binarios} controller/a01_preproceso.py")


# Container_de_la_app ---------------------------------------- 
os.system(f"streamlit run container/b01_container_streamlit.py")


