from PyQt5 import QtCore, QtGui, QtWidgets
import Backend
    
class Ui_MainWindow(object):
    
    def __init__(self):
        #eventos de una fecha, se debe cargar cada vez que se cambia de fecha
        self.eventos = list()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(10, 10, 400, 250))
        self.calendario.setGridVisible(False)
        self.calendario.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.calendario.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendario.setNavigationBarVisible(True)
        self.calendario.setDateEditEnabled(True)
        self.calendario.setObjectName("calendario")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(430, 10, 461, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 20, 60, 30))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 60, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 60, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(19, 140, 81, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.text_nombre = QtWidgets.QLineEdit(self.frame)
        self.text_nombre.setGeometry(QtCore.QRect(110, 60, 113, 30))
        self.text_nombre.setObjectName("text_hora")
        self.text_tipo = QtWidgets.QLineEdit(self.frame)
        self.text_tipo.setGeometry(QtCore.QRect(110, 100, 113, 30))
        self.text_tipo.setObjectName("text_asunto")
        self.text_descripcion = QtWidgets.QTextEdit(self.frame)
        self.text_descripcion.setGeometry(QtCore.QRect(110, 140, 291, 111))
        self.text_descripcion.setObjectName("text_nota")
        self.text_fecha = QtWidgets.QDateEdit(self.frame)
        self.text_fecha.setGeometry(QtCore.QRect(110, 20, 113, 30))
        self.text_fecha.setCalendarPopup(False)
        self.text_fecha.setObjectName("text_fecha")
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setGeometry(QtCore.QRect(130, 260, 88, 34))
        self.btn_save.setObjectName("btn_save")
        self.btn_delete = QtWidgets.QPushButton(self.frame)
        self.btn_delete.setGeometry(QtCore.QRect(260, 260, 88, 34))
        self.btn_delete.setObjectName("btn_delete")
        self.lista = QtWidgets.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(10, 310, 400, 250))
        self.lista.setObjectName("lista")
        self.btn_add_evtn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_evtn.setGeometry(QtCore.QRect(150, 270, 111, 34))
        self.btn_add_evtn.setObjectName("btn_add_evtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #cargar fecha actual al text_fecha
        self.text_fecha.setDate(self.calendario.selectedDate())
        
        #agregar acciones a los eventos
        self.calendario.clicked.connect(self.date_changed)
        self.btn_add_evtn.clicked.connect(self.btn_add_evtn_click)
        self.lista.itemClicked.connect(self.item_click)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calendario"))
        self.label.setText(_translate("MainWindow", "Fecha:"))
        self.label_2.setText(_translate("MainWindow", "Nombre:"))
        self.label_3.setText(_translate("MainWindow", "Tipo:"))
        self.label_4.setText(_translate("MainWindow", "Descripcion:"))
        self.text_fecha.setDisplayFormat(_translate("MainWindow", "d/MM/yyyy"))
        self.btn_save.setText(_translate("MainWindow", "Guardar"))
        self.btn_delete.setText(_translate("MainWindow", "Eliminar"))
        self.btn_add_evtn.setText(_translate("MainWindow", "Agregar Evento"))
        
        
    #accion boton agregar
    def btn_add_evtn_click(self):
        self.text_fecha.setDate(self.calendario.selectedDate())
    
    #que hacer cuando se cambia la fecha en el calendario
    def date_changed(self):
        #borrar campos
        self.text_fecha.setDate(self.calendario.selectedDate())
        self.text_tipo.setText("")
        self.text_nombre.setText("")
        self.text_descripcion.setText("")
        
        #cargar lista de eventos de la fecha elegida
        
    def item_click(self, item):
        pass


    def cargar_eventos(self, fecha):
        pass
    
    def crear_fecha(self, fecha: str):
        lista = fecha.split()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
