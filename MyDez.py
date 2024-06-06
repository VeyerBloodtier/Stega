import hamming
import precoder
from zipfile import ZipFile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QGraphicsPixmapItem, QPixmap, QGraphicsScene

asysy = []
wayy = ["", ""]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        # self.comboBox = QtWidgets.QComboBox(self.tab)
        # self.comboBox.setObjectName("comboBox")
        # self.verticalLayout_4.addWidget(self.comboBox)
        self.item_enc = QtWidgets.QListWidget(self.tab)
        self.item_enc.setObjectName("item_enc")
        self.verticalLayout_4.addWidget(self.item_enc)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add = QtWidgets.QPushButton(self.tab)
        self.add.setObjectName("add")
        self.verticalLayout_3.addWidget(self.add)
        self.rem = QtWidgets.QPushButton(self.tab)
        self.rem.setObjectName("rem")
        self.verticalLayout_3.addWidget(self.rem)
        self.calear = QtWidgets.QPushButton(self.tab)
        self.calear.setObjectName("calear")
        self.verticalLayout_3.addWidget(self.calear)
        self.enc = QtWidgets.QPushButton(self.tab)
        self.enc.setObjectName("enc")
        self.verticalLayout_3.addWidget(self.enc)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.way = QtWidgets.QLabel(self.tab)
        self.way.setObjectName("way")
        self.horizontalLayout_2.addWidget(self.way)
        self.cont = QtWidgets.QPushButton(self.tab)
        self.cont.setMaximumSize(QtCore.QSize(120, 16777215))
        self.cont.setObjectName("cont")
        self.horizontalLayout_2.addWidget(self.cont)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lsbr = QtWidgets.QRadioButton(self.tab)
        self.lsbr.setObjectName("lsbr")
        self.horizontalLayout.addWidget(self.lsbr)
        self.lsbm = QtWidgets.QRadioButton(self.tab)
        self.lsbm.setObjectName("lsbm")
        self.horizontalLayout.addWidget(self.lsbm)
        self.ham = QtWidgets.QRadioButton(self.tab)
        self.ham.setObjectName("ham")
        self.horizontalLayout.addWidget(self.ham)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.img_enc = QtWidgets.QGraphicsView(self.tab)
        self.img_enc.setObjectName("img_enc")
        self.horizontalLayout_4.addWidget(self.img_enc)
        self.img_full = QtWidgets.QGraphicsView(self.tab)
        self.img_full.setObjectName("img_full")
        self.horizontalLayout_4.addWidget(self.img_full)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.chuse = QtWidgets.QPushButton(self.tab_2)
        self.chuse.setObjectName("chuse")
        self.verticalLayout_6.addWidget(self.chuse)
        self.dec = QtWidgets.QPushButton(self.tab_2)
        self.dec.setObjectName("dec")
        self.verticalLayout_6.addWidget(self.dec)
        self.decaps = QtWidgets.QPushButton(self.tab_2)
        self.decaps.setObjectName("decaps")
        self.verticalLayout_6.addWidget(self.decaps)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.img_dec = QtWidgets.QGraphicsView(self.tab_2)
        self.img_dec.setObjectName("img_dec")
        self.horizontalLayout_6.addWidget(self.img_dec)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.item_dec = QtWidgets.QListWidget(self.tab_2)
        self.item_dec.setObjectName("item_dec")
        self.verticalLayout_8.addWidget(self.item_dec)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Скрываемая информация"))
        self.add.setText(_translate("MainWindow", "Добавить файл"))
        self.rem.setText(_translate("MainWindow", "Удалить файл"))
        self.calear.setText(_translate("MainWindow", "Очистить"))
        self.enc.setText(_translate("MainWindow", "Сокрыть информацию"))
        self.way.setText(_translate("MainWindow", "Контейнер: -"))
        self.cont.setText(_translate("MainWindow", "Выбрать"))
        self.lsbr.setText(_translate("MainWindow", "LSB-R"))
        self.lsbm.setText(_translate("MainWindow", "LSB-M"))
        self.ham.setText(_translate("MainWindow", "Код Хэминга"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Сокрытие данных"))
        self.label_2.setText(_translate("MainWindow", "Контейнер"))
        self.chuse.setText(_translate("MainWindow", "Выбрать"))
        self.dec.setText(_translate("MainWindow", "Извлечь данные"))
        self.decaps.setText(_translate("MainWindow", "Записать в папку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Извлечение данных"))

        self.addfunk()

    def addfunk(self):
        # Сокрыттие
        self.add.clicked.connect(self.add_file)  # добавить
        self.rem.clicked.connect(self.rem_file)  # убрать
        self.calear.clicked.connect(self.cler_file)  # очистить
        self.enc.clicked.connect(self.encaps)  # сокрыть
        self.cont.clicked.connect(self.contsel)  # продолжить
        # Извлечение
        self.chuse.clicked.connect(self.select)  # Выбор
        self.dec.clicked.connect(self.decap)  # Извлеч данные
        self.decaps.clicked.connect(self.decapsulate)  # Записать данные
        # self.LoadBTN.clicked.connect(self.tabload)

        pass

    def add_file(self):
        met = QtWidgets.QFileDialog.getOpenFileName()[0]
        mem = True
        for i in range(len(asysy)):
            if asysy[i] == met:
                mem = False
        if mem:
            asysy.append(met)
            self.item_enc.clear()
            self.item_enc.addItems(asysy)
        # print(asysy)
        # pass

    def rem_file(self):
        met = QtWidgets.QFileDialog.getOpenFileName()[0]
        for i in range(len(asysy)):
            if asysy[i] == met:
                asysy.pop(i)
                self.item_enc.clear()
                self.item_enc.addItems(asysy)
                break
        # print(asysy)

    def cler_file(self):
        # print(asysy)
        self.item_enc.clear()
        asysy.clear()
        # print(asysy)

    def encaps(self):
        myzip = ZipFile("Karandash.zip", "w")
        for i in asysy:
            myzip.write(i.split("/")[-1])
        myzip.close()
        # print(wayy[0])
        if wayy[0] != "":
            # print(wayy[0])
            if self.lsbr.isChecked():
                # print(wayy[0])
                precoder.LSBR(wayy[0], precoder.butch("Karandash.zip"))
                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap("eggs.bmp").scaled(476, 256))
                scen = QGraphicsScene()
                scen.addItem(pic)
                self.img_enc.setScene(scen)
                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap(wayy[0]).scaled(476, 256))
                scen = QGraphicsScene()
                scen.addItem(pic)
                self.img_full.setScene(scen)
            if self.lsbm.isChecked():
                # print(wayy[0])
                precoder.LSBM(wayy[0], precoder.butch("Karandash.zip"))
                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap("eggs.bmp").scaled(476, 256))
                scen = QGraphicsScene()
                scen.addItem(pic)
                self.img_enc.setScene(scen)
                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap(wayy[0]).scaled(476, 256))
                scen = QGraphicsScene()
                scen.addItem(pic)
                self.img_full.setScene(scen)
            if self.ham.isChecked():
                # print(wayy[0])
                precoder.LSBM(wayy[0], precoder.butch("Karandash.zip"))
                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap("eggs.bmp").scaled(476, 256))
                scen = QGraphicsScene()
                scen.addItem(pic)
                self.img_enc.setScene(scen)
                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap(wayy[0]).scaled(476, 256))
                scen = QGraphicsScene()
                scen.addItem(pic)
                self.img_full.setScene(scen)

    def contsel(self):
        met = QtWidgets.QFileDialog.getOpenFileName()[0]
        if met.split(".")[-1] == "bmp":
            # print(met)
            wayy[0] = met
            self.way.setText("Контейнер: " + met + " Ёмкость: " + str(precoder.max_size_show(wayy[0], 1)) + " бит")
        else:
            self.way.setText("Контейнер: " + "Выбран не bmp - файл")

    def select(self):
        met = QtWidgets.QFileDialog.getOpenFileName()[0]
        if met.split(".")[-1] == "bmp":
            pic = QGraphicsPixmapItem()
            pic.setPixmap(QPixmap(met).scaled(476, 256))
            scen = QGraphicsScene()
            scen.addItem(pic)
            self.img_dec.setScene(scen)
            wayy[1] = met

    def decap(self):
        if wayy[1] != "":
            precoder.silck("eggs.zip", precoder.DLSBR(wayy[1]))
            myzip = ZipFile("eggs.zip", "r")
            self.item_dec.clear()
            self.item_dec.addItems(myzip.namelist())

    def decapsulate(self):
        met = QtWidgets.QFileDialog.getExistingDirectory()
        if wayy[1] != "":
            precoder.silck(met + "\\" + "eggs.zip", precoder.DLSBR(wayy[1]))
            myzip = ZipFile(met + "\\" + "eggs.zip", "r")
            self.item_dec.clear()
            # print(myzip.namelist())
            self.item_dec.addItems(myzip.namelist())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    pass
