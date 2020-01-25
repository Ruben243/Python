# importamos de nuestro archivo creado
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from SaludoGrafico import *


# constructor que hereda de QDialog
class SaludoApp(QDialog):
    # constructor
    def __init__(self):
        # contructor clase padre
        super().__init__()

        # creamos objeto de nuestra clase del archivo creado con Qt desitner
        self.saludo = Ui_Form()
        # inicializamos la interfac setUI presente en el archivo creado con QT designer
        self.saludo.setupUi(self)
        # manipulalor de eventos asignado al boton.Al hacer clieck ejecuta la funcion mostrar_text
        self.saludo.pushButton.clicked.connect(self.mostrar_text)
        # mostramos el texto
        self.show()

    # funcion que muestra el saludo
    def mostrar_text(self):
        # obtenemos el texto del campo de texto Text con la funcion Text()
        mensaje = self.saludo.Text.text()
        # asignamos el texto a la etiuet donde mostrarlo
        self.saludo.Saludoout.setText(mensaje)


# creamos la aplicacion sobre el modulo actual
if __name__ == '__main__':
    #creamos una instancia de QApplication con los argumentos que se pasan desde la line de comandos
    app = QApplication(sys.argv)
    #creamos el saludo que creamos en la clase SaludoApp()
    saludo = SaludoApp()
    #mostramos la instancia
    saludo.show()
    #evento de salida
    sys.exit(app.exec_())
