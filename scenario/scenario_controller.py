import sys
from scenario_map import scenario_data
import generator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap


class Ui_Controller(object):
    map_list = []
    weather_list = []
    traffic_situ = []
    des_sce = ""
    des_map = ""
    current_scenario = {}
    current_map = "Town01"
    current_weather = "Default"
    current_traffic = "smooth"
    simulation_time = 3
    current_a1 = ""
    current_a2 = ""
    current_a3 = ""
    anomaly_pos = ""
    false_pos = ""
    false_neg = ""

    def setupUi(self, Controller):
        Controller.setObjectName("Controller")
        Controller.resize(657, 770)
        self.scenarios = QtWidgets.QComboBox(Controller)
        self.scenarios.setGeometry(QtCore.QRect(130, 60, 121, 22))
        self.scenarios.setObjectName("scenarios")
        self.scenarios.addItems(scenario_data.scenarios)
        self.scenarios.currentIndexChanged.connect(self.decide_scenario)
        self.label = QtWidgets.QLabel(Controller)
        self.label.setGeometry(QtCore.QRect(40, 60, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Controller)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 71, 21))
        self.label_2.setObjectName("label_2")
        self.maps = QtWidgets.QComboBox(Controller)
        self.maps.setGeometry(QtCore.QRect(130, 100, 121, 22))
        self.maps.setObjectName("maps")
        self.maps.currentIndexChanged.connect(self.decide_map)
        self.label_3 = QtWidgets.QLabel(Controller)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 131, 31))
        self.label_3.setObjectName("label_3")
        self.generate_scenario = QtWidgets.QPushButton(Controller)
        self.generate_scenario.setGeometry(QtCore.QRect(510, 720, 101, 23))
        self.generate_scenario.setObjectName("generate_scenario")
        self.generate_scenario.clicked.connect(self.decide_final)
        self.weathers = QtWidgets.QComboBox(Controller)
        self.weathers.setGeometry(QtCore.QRect(130, 140, 121, 22))
        self.weathers.setObjectName("weathers")
        self.weathers.currentIndexChanged.connect(self.decide_weather)
        self.situations = QtWidgets.QComboBox(Controller)
        self.situations.setGeometry(QtCore.QRect(538, 90, 71, 22))
        self.situations.setObjectName("situations")
        self.situations.currentIndexChanged.connect(self.decide_traffic)
        self.label_8 = QtWidgets.QLabel(Controller)
        self.label_8.setGeometry(QtCore.QRect(40, 140, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Controller)
        self.label_9.setGeometry(QtCore.QRect(420, 90, 111, 21))
        self.label_9.setObjectName("label_9")
        self.exit = QtWidgets.QPushButton(Controller)
        self.exit.setGeometry(QtCore.QRect(40, 720, 75, 23))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.leave)
        self.label_10 = QtWidgets.QLabel(Controller)
        self.label_10.setGeometry(QtCore.QRect(420, 50, 101, 21))
        self.label_10.setObjectName("label_10")
        self.descriptions = QtWidgets.QTextBrowser(Controller)
        self.descriptions.setGeometry(QtCore.QRect(40, 180, 571, 151))
        self.descriptions.setObjectName("descriptions")
        self.times = QtWidgets.QLineEdit(Controller)
        self.times.setGeometry(QtCore.QRect(540, 50, 71, 21))
        self.times.setObjectName("times")
        self.times.setAlignment(QtCore.Qt.AlignRight)
        self.label_4 = QtWidgets.QLabel(Controller)
        self.label_4.setGeometry(QtCore.QRect(40, 550, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Controller)
        self.label_5.setGeometry(QtCore.QRect(40, 590, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Controller)
        self.label_6.setGeometry(QtCore.QRect(40, 630, 161, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Controller)
        self.comboBox.setGeometry(QtCore.QRect(430, 550, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(scenario_data.possibilities)
        self.comboBox_2 = QtWidgets.QComboBox(Controller)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 590, 181, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(scenario_data.possibilities)
        self.comboBox_3 = QtWidgets.QComboBox(Controller)
        self.comboBox_3.setGeometry(QtCore.QRect(430, 630, 181, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(scenario_data.possibilities)
        self.anomaly_1 = QtWidgets.QLabel(Controller)
        self.anomaly_1.setGeometry(QtCore.QRect(110, 355, 300, 30))
        self.anomaly_1.setText("")
        self.anomaly_1.setObjectName("anomaly_1")
        self.anomaly_2 = QtWidgets.QLabel(Controller)
        self.anomaly_2.setGeometry(QtCore.QRect(110, 425, 300, 30))
        self.anomaly_2.setText("")
        self.anomaly_2.setObjectName("anomaly_2")
        self.anomaly_3 = QtWidgets.QLabel(Controller)
        self.anomaly_3.setGeometry(QtCore.QRect(110, 495, 300, 30))
        self.anomaly_3.setText("")
        self.anomaly_3.setObjectName("anomaly_3")
        self.icon_1 = QtWidgets.QLabel(Controller)
        self.icon_1.setGeometry(QtCore.QRect(40, 340, 60, 60))
        self.icon_1.setText("")
        self.icon_1.setObjectName("icon_1")
        self.icon_2 = QtWidgets.QLabel(Controller)
        self.icon_2.setGeometry(QtCore.QRect(40, 410, 60, 60))
        self.icon_2.setText("")
        self.icon_2.setObjectName("icon_2")
        self.icon_3 = QtWidgets.QLabel(Controller)
        self.icon_3.setGeometry(QtCore.QRect(40, 480, 60, 60))
        self.icon_3.setText("")
        self.icon_3.setObjectName("icon_3")

        self.current_scenario = eval("scenario_data."+self.scenarios.currentText())

        self.retranslateUi(Controller)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    def retranslateUi(self, Controller):
        _translate = QtCore.QCoreApplication.translate
        Controller.setWindowTitle(_translate("Controller", "Carla simulator scenario controller"))
        self.label.setText(_translate("Controller", "Select a senario*"))
        self.label_2.setText(_translate("Controller", "Select a map"))
        self.label_3.setText(_translate("Controller", "Carla scenario controller"))
        self.generate_scenario.setText(_translate("Controller", "Generate scenario"))
        self.label_8.setText(_translate("Controller", "Select weather"))
        self.label_9.setText(_translate("Controller", "Select traffic situation"))
        self.exit.setText(_translate("Controller", "Exit"))
        self.label_10.setText(_translate("Controller", "Simulation time(min)"))
        self.descriptions.setHtml(_translate("Controller", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To launch the simulation,you have to at least select a scenario.</span></p></body></html>"))
        self.label_4.setText(_translate("Controller", "Anomaly generation rate"))
        self.label_5.setText(_translate("Controller", "False possitive rate"))
        self.label_6.setText(_translate("Controller", "False negative rate"))

    def decide_scenario(self):
        self.current_scenario = eval("scenario_data."+self.scenarios.currentText())
        if self.current_scenario['name'] == "Nothing":
            self.map_list = []
            self.weather_list = []
            self.traffic_situ = []
            self.des_sce = "To launch the simulation,you have to at least select a scenario."
            self.des_map = ""
            self.current_a1 = ""
            self.current_a2 = ""
            self.current_a3 = ""
            pixmap = QPixmap("")
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
            self.anomaly_1.setText(self.current_a1)
            self.anomaly_2.setText(self.current_a2)
            self.anomaly_3.setText(self.current_a3)
            self.icon_1.setPixmap(pixmap)
            self.icon_2.setPixmap(pixmap)
            self.icon_3.setPixmap(pixmap)
            self.icon_1.resize(60,60)
            self.icon_1.setScaledContents(True)
            self.icon_2.resize(60,60)
            self.icon_2.setScaledContents(True)
            self.icon_3.resize(60,60)
            self.icon_3.setScaledContents(True)
        if self.current_scenario['name'] == "scenario_1":
            self.map_list = scenario_data.map_normal
            self.weather_list = scenario_data.weather_fine
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_1
            self.des_map = scenario_data.map_info1
            self.current_a1 = "Door not closed:You can see vehicle door opening."
            self.current_a2 = "Unwear Seatbelt:The autopiloy won't apply if happens."
            self.current_a3 = "Coolant temperature abnormal:Irregularly accelerate or desending speed."
            pixmap_1 = QPixmap("./Icons/door.png")
            pixmap_2 = QPixmap("./Icons/seatbelt.png")
            pixmap_3 = QPixmap("./Icons/coolant.png")
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
            self.anomaly_1.setText(self.current_a1)
            self.anomaly_2.setText(self.current_a2)
            self.anomaly_3.setText(self.current_a3)
            self.icon_1.setPixmap(pixmap_1)
            self.icon_2.setPixmap(pixmap_2)
            self.icon_3.setPixmap(pixmap_3)
            self.icon_1.resize(60,60)
            self.icon_1.setScaledContents(True)
            self.icon_2.resize(60,60)
            self.icon_2.setScaledContents(True)
            self.icon_3.resize(60,60)
            self.icon_3.setScaledContents(True)
        if self.current_scenario['name'] == "scenario_2":
            self.map_list = scenario_data.map_normal
            self.weather_list = scenario_data.weather_fine
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_2
            self.des_map = scenario_data.map_info1
            self.current_a1 = "Engine problems:The car stops completely."
            self.current_a2 = "Fuel/Battery not enough:Very low speed driving."
            self.current_a3 = "Brake system problems:The car will ignore red traffic lights."
            pixmap_1 = QPixmap("./Icons/engine.png")
            pixmap_2 = QPixmap("./Icons/fuel.png")
            pixmap_3 = QPixmap("./Icons/brake.png")
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
            self.anomaly_1.setText(self.current_a1)
            self.anomaly_2.setText(self.current_a2)
            self.anomaly_3.setText(self.current_a3)
            self.icon_1.setPixmap(pixmap_1)
            self.icon_2.setPixmap(pixmap_2)
            self.icon_3.setPixmap(pixmap_3)
            self.icon_1.resize(60,60)
            self.icon_1.setScaledContents(True)
            self.icon_2.resize(60,60)
            self.icon_2.setScaledContents(True)
            self.icon_3.resize(60,60)
            self.icon_3.setScaledContents(True)
        if self.current_scenario['name'] == "scenario_3":
            self.map_list = scenario_data.map_highway
            self.weather_list = scenario_data.weather_fine
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_3
            self.des_map = scenario_data.map_info1
            self.current_a1 = "Engine problems:The car stops completely."
            self.current_a2 = "Fuel/Battery not enough:Very low speed driving."
            self.current_a3 = "Brake system problems:The car will ignore red traffic lights."
            pixmap_1 = QPixmap("./Icons/engine.png")
            pixmap_2 = QPixmap("./Icons/fuel.png")
            pixmap_3 = QPixmap("./Icons/brake.png")
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
            self.anomaly_1.setText(self.current_a1)
            self.anomaly_2.setText(self.current_a2)
            self.anomaly_3.setText(self.current_a3)
            self.icon_1.setPixmap(pixmap_1)
            self.icon_2.setPixmap(pixmap_2)
            self.icon_3.setPixmap(pixmap_3)
            self.icon_1.resize(60,60)
            self.icon_1.setScaledContents(True)
            self.icon_2.resize(60,60)
            self.icon_2.setScaledContents(True)
            self.icon_3.resize(60,60)
            self.icon_3.setScaledContents(True)
        if self.current_scenario['name'] == "scenario_4":
            self.map_list = scenario_data.map_all
            self.weather_list = scenario_data.weather_bad
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_4
            self.des_map = scenario_data.map_info1
            self.current_a1 = "Engine problems:The car stops completely."
            self.current_a2 = "Fuel/Battery not enough:Very low speed driving."
            self.current_a3 = "Brake system problems:The car will ignore red traffic lights."
            pixmap_1 = QPixmap("./Icons/engine.png")
            pixmap_2 = QPixmap("./Icons/fuel.png")
            pixmap_3 = QPixmap("./Icons/brake.png")
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
            self.anomaly_1.setText(self.current_a1)
            self.anomaly_2.setText(self.current_a2)
            self.anomaly_3.setText(self.current_a3)
            self.icon_1.setPixmap(pixmap_1)
            self.icon_2.setPixmap(pixmap_2)
            self.icon_3.setPixmap(pixmap_3)
            self.icon_1.resize(60,60)
            self.icon_1.setScaledContents(True)
            self.icon_2.resize(60,60)
            self.icon_2.setScaledContents(True)
            self.icon_3.resize(60,60)
            self.icon_3.setScaledContents(True)

    def decide_map(self):
        self.current_map = self.maps.currentText()
        if self.current_map == "Town01":
            self.des_map = scenario_data.map_info1
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_map == "Town02":
            self.des_map = scenario_data.map_info2
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_map == "Town03":
            self.des_map = scenario_data.map_info3
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_map == "Town04":
            self.des_map = scenario_data.map_info4
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_map == "Town05":
            self.des_map = scenario_data.map_info5
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_map == "Town06":
            self.des_map = scenario_data.map_info6
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_map == "Town07":
            self.des_map = scenario_data.map_info7
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_map == "Town10HD":
            self.des_map = scenario_data.map_info10
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)

    def decide_traffic(self):
        self.current_traffic = self.situations.currentText()

    def decide_weather(self):
        self.current_weather = self.weathers.currentText()

    def decide_final(self):
        if self.current_scenario['name'] != "Nothing":
            if self.times.text() != "":
                self.simulation_time = int(self.times.text())
            if self.comboBox.currentText() != "":
                self.anomaly_pos = self.comboBox.currentText()
            if self.comboBox_2.currentText() != "":
                self.false_pos = self.comboBox_2.currentText()
            if self.comboBox_3.currentText() != "":
                self.false_neg = self.comboBox_3.currentText()
            if self.simulation_time > 20 or self.simulation_time < 3:
                msg = QMessageBox()
                msg.setWindowTitle("Invalid simulation time.")
                msg.setText("The simulation time should be 3~20 mins.")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec()
            else:
                print(self.current_scenario['name'],self.current_map,self.current_traffic,self.current_weather)
                print("time:",self.simulation_time,"anomaly:",self.anomaly_pos,"false positive:",self.false_pos,"false negative:",self.false_neg)
                generator.generate_scenario(self.current_scenario,self.current_map,self.current_weather,self.simulation_time,self.current_traffic,self.anomaly_pos,self.false_pos,self.false_neg)
                sys.exit()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid scenario.")
            msg.setText("You should at least select a scenario.")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec()

    def leave(self):
        QApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    w = Ui_Controller()
    w.setupUi(mainwindow)

    mainwindow.show()
    sys.exit(app.exec_())
