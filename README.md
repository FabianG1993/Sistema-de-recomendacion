# Sistema-de-recomendacion
Este proyecto consiste en un modelo que sirve como herramienta para recomendar cultivos a partir de propiedades del suelo y el medio ambiente. 

## En qué consiste el modelo

1. **Carga de Datos**: Es un archivo .csv con valores relacionados a las caracteristicas del suelo y el ambiente.

2. **Procesamiento de Datos**: Una vez se ingresan los datos, se procesa la información y se prepara para aplicar el modelo SVM. Esto incluye aplicar train_test_split para dividir el conjunto de datos en conjunto de entrenamiento y prueba.

3. **Clasificación con SVM**: Se entrena el modelo SVM con los datos proporcionados. El modelo analiza los patrones y las relaciones entre los diferentes parámetros.

4. **Evaluación del modelo**: Se aplico accuracy(número de predicciones correctas dividido por el número total de predicciones) para la evaluacion del modelo. Se obtuvo un score de 0.993. 

5. **Guadar modelo**: Se procede a guardar el modelo en formato .pickle para posteriomente llevarlo a nuestra aplicación. 

## En qué consiste la interfaz 

La interfaz gráfica de usuario (GUI) desarrollado en Python utilizando la biblioteca PyQt5. Esta permite a los usuarios ingresar valores relacionados con características agrícolas de los suelos y el ambiente (como niveles de nutrientes (minerales), temperatura, humedad, etc.), y luego utiliza un modelo de máquina de soporte vectorial (SVM) previamente entrenado para realizar recomendaciones sobre qué cultivo es adecuado según los valores ingresados. 

## Cómo Utilizar

1. Ejecuta el archivo interfaz.py.
2. Ingresa los datos requeridos.
3. Haz clic en el botón "Recomendar".
4. Haz clic en "Reiniciar" para nuevas recomendaciones. 

## Requisitos del Sistema

- Python en su versión más reciente. 
- IDE (entorno de desarrollo integrado).

## Uso

Si deseas ejecutar la aplicación puedes seguir estos pasos:

1. Clona este repositorio en tu ordenador.
2. Asegúrate de tener Python instalado y las bibliotecas necesarias.
3. Abre el archivo .ipynb en un entorno Jupyter Notebook.
4. Ejecuta las celdas para cargar y guardar el modelo.
5. Ejecuta el archivo interfaz.py.
5. Usa el aplicativo.

## Notas

- Este proyecto tiene fines informativos y/o educativos. Los resultados de las recomendaciones pueden variar y no deben utilizarse como base única para tomar decisiones importantes.

## Créditos

- Autor: Fabián García Gómez
- Contacto: datasolu7ion@gmail.com
