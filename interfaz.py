import sys
import pickle
import numpy as np
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QMessageBox, QPushButton, QStatusBar

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # crear labels por cada caracteristica
        self.labels = [QLabel("Nitrogeno"), QLabel("Fosforo"), QLabel("Calcio"), 
                       QLabel("Temperatura"), QLabel("Humedad"), QLabel("Ph"), 
                       QLabel("Lluvias")]
        # crear input boxes para cada label
        self.input_boxes = [QLineEdit() for label in self.labels]
        # montar los labels a la ventana
        self.layout = QVBoxLayout()
        for label, input_box in zip(self.labels, self.input_boxes):
            self.layout.addWidget(label)
            self.layout.addWidget(input_box)
        self.setLayout(self.layout)
        # crear boton para hacer recomendación
        self.predict_button = QPushButton("Recomendar")
        self.predict_button.clicked.connect(self.predict)
        self.layout.addWidget(self.predict_button)
        self.predict_button.setFont(QtGui.QFont("Arial", 11)) #cambiar tamaño de fuente
        self.predict_button.setStyleSheet("background-color: green; color: white; width: 80px; margin-top: 10px;")
        self.predict_button.setFixedWidth(100)
        # crear label para el valor de salida
        self.prediction_label = QLabel("Se recomienda cultivar:")
        self.layout.addWidget(self.prediction_label)
        self.prediction_label.setFont(QtGui.QFont("Arial", 11)) #cambiar tamaño de fuente
        # crear boton para borrar formulario
        self.clear_button = QPushButton("Reiniciar")
        self.clear_button.clicked.connect(self.clear_inputs)
        self.layout.addWidget(self.clear_button)
        self.clear_button.setFont(QtGui.QFont("Arial", 11))
        self.clear_button.setStyleSheet("background-color:blue; color:white; width:80px; margin-top: 10px;")
        self.clear_button.setFixedWidth(100)
        # agregar icono a la interfaz
        icon_path = "D:\Sistema de recomendacion SVM\icono.ico"  # Cambia esto a la ruta de tu archivo de icono
        self.setWindowIcon(QtGui.QIcon(icon_path))
        # cambiar tamaño de fuente
        font = self.font()
        font.setPointSize(11)
        for label, input_box in zip(self.labels, self.input_boxes):
            label.setFont(font)
            input_box.setFont(font)
        # cambiar color de fondo
        self.setStyleSheet("background-color: white;")
        # cargar modelo ML
        self.model = pickle.load(open("svm_model.pkl", "rb"))
        # validador para aceptar solo inputs numericos
        for input_box in self.input_boxes:
            input_box.setValidator(QDoubleValidator())
    '''
    Función predict toma valores ingresados por el usuario que representan diferentes 
    características relacionadas con la agricultura (nitrogeno, temperatura, humedad, 
    pH, entre otros.), pasa estos valores a través de un modelo para hacer una predicción
    y luego muestra la predicción en una etiqueta en la interfaz gráfica.
    '''
    def predict(self):
        # bbtener valores ingresados
        nitrogeno = self.input_boxes[0].text()
        fosforo = self.input_boxes[1].text()
        calcio = self.input_boxes[2].text()
        temperatura = self.input_boxes[3].text()
        humedad = self.input_boxes[4].text()
        ph = self.input_boxes[5].text()
        lluvias = self.input_boxes[6].text()
        # validar que los campos sean llenados por completo
        if not all([nitrogeno, fosforo, calcio, temperatura, humedad, ph, lluvias]):
            QMessageBox.warning(self, "Advertencia", "Por favor ingrese todos los valores.")
            return
        # transformar datos
        nitrogeno = float(nitrogeno)
        fosforo = float(fosforo)
        calcio = float(calcio)
        temperatura = float(temperatura)
        humedad = float(humedad)
        ph = float(ph)
        lluvias = float(lluvias)
        # desplegar modelo
        x_in = np.asarray([nitrogeno, fosforo, calcio, temperatura, 
                           humedad, ph, lluvias]).reshape(1,-1)
        prediction = self.model.predict(x_in)
        # mostrar la salida
        self.prediction_label.setText("Se recomienda cultivar: " + prediction[0])
    '''
    Función clear_inputs realiza un ciclo a través de todas las cajas de entrada de una 
    interfaz gráfica y borra el contenido de cada una de ellas. Además, también borra el 
    contenido de una etiqueta de predicción.
    '''
    def clear_inputs(self):
        for input_box in self.input_boxes:
            input_box.clear()
        self.prediction_label.clear()
    '''
    Función show muestra la interfaz gráfica de la aplicación y luego inicia el bucle de 
    eventos de la aplicación. Cuando el usuario interactúa con la interfaz, el bucle de 
    eventos garantiza que la aplicación responda de manera adecuada y fluida. Al finalizar 
    la interacción y cerrar la ventana, la función sys.exit() se utiliza para salir de la 
    aplicación de manera limpia, asegurándose de que los recursos se liberen y la aplicación
    se cierre adecuadamente.
    '''
    def show(self):
        super().show()
        sys.exit(QApplication.exec_())

if __name__ == "__main__":
    # crear aplicación
    app = QApplication(sys.argv)
    app.setApplicationName("SISTEMA DE RECOMENDACIÓN DE CULTIVOS")
    # crear una ventana-interfaz
    main_window = MainWindow()
    # cambiar el tamaño de la ventana principal al iniciar
    main_window.resize(500, 600)
    # mostrar ventana
    main_window.show()
    # iniciar / terminar
    sys.exit(app.exec_())
