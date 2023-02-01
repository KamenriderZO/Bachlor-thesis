import sys
from scenario_map import scenario_data
import generator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtWidgets import QMessageBox

class Ui_Controller(object):
    map_list = []
    weather_list = []
    traffic_situ = []
    des_sce = ""
    des_map = ""
    anomaly_pos = 0
    false_pos = 0
    false_neg = 0

    current_scenario = {}
    current_map = "Town01"
    current_weather = "Default"
    current_traffic = "smooth"
    simulation_time = 3
    def setupUi(self, Controller):
        Controller.setObjectName("Controller")
        Controller.resize(491, 603)
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
        self.generate_scenario.setGeometry(QtCore.QRect(350, 560, 101, 23))
        self.generate_scenario.setObjectName("generate_scenario")
        self.generate_scenario.clicked.connect(self.decide_final)
        self.weathers = QtWidgets.QComboBox(Controller)
        self.weathers.setGeometry(QtCore.QRect(130, 140, 121, 22))
        self.weathers.setObjectName("weathers")
        self.weathers.currentIndexChanged.connect(self.decide_weather)
        self.situations = QtWidgets.QComboBox(Controller)
        self.situations.setGeometry(QtCore.QRect(378, 100, 71, 22))
        self.situations.setObjectName("situations")
        self.situations.currentIndexChanged.connect(self.decide_traffic)
        self.label_8 = QtWidgets.QLabel(Controller)
        self.label_8.setGeometry(QtCore.QRect(40, 140, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Controller)
        self.label_9.setGeometry(QtCore.QRect(260, 100, 111, 21))
        self.label_9.setObjectName("label_9")
        self.exit = QtWidgets.QPushButton(Controller)
        self.exit.setGeometry(QtCore.QRect(40, 560, 75, 23))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.leave)
        self.label_10 = QtWidgets.QLabel(Controller)
        self.label_10.setGeometry(QtCore.QRect(260, 60, 101, 21))
        self.label_10.setObjectName("label_10")
        self.descriptions = QtWidgets.QTextBrowser(Controller)
        self.descriptions.setGeometry(QtCore.QRect(40, 180, 411, 181))
        self.descriptions.setObjectName("descriptions")
        self.times = QtWidgets.QLineEdit(Controller)
        self.times.setGeometry(QtCore.QRect(380, 60, 71, 21))
        self.times.setObjectName("times")
        self.times.setAlignment(QtCore.Qt.AlignRight)
        self.label_4 = QtWidgets.QLabel(Controller)
        self.label_4.setGeometry(QtCore.QRect(40, 390, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Controller)
        self.label_5.setGeometry(QtCore.QRect(40, 430, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Controller)
        self.label_6.setGeometry(QtCore.QRect(40, 470, 161, 16))
        self.label_6.setObjectName("label_6")
        self.anomaly_possibility = QtWidgets.QLineEdit(Controller)
        self.anomaly_possibility.setGeometry(QtCore.QRect(220, 390, 113, 20))
        self.anomaly_possibility.setObjectName("anomaly_possibility")
        self.anomaly_possibility.setAlignment(QtCore.Qt.AlignRight)
        self.false_positive = QtWidgets.QLineEdit(Controller)
        self.false_positive.setGeometry(QtCore.QRect(220, 430, 113, 20))
        self.false_positive.setObjectName("false_positive")
        self.false_positive.setAlignment(QtCore.Qt.AlignRight)
        self.false_negative = QtWidgets.QLineEdit(Controller)
        self.false_negative.setGeometry(QtCore.QRect(220, 470, 113, 20))
        self.false_negative.setObjectName("false_negative")
        self.false_negative.setAlignment(QtCore.Qt.AlignRight)
        self.label_11 = QtWidgets.QLabel(Controller)
        self.label_11.setGeometry(QtCore.QRect(340, 390, 51, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Controller)
        self.label_12.setGeometry(QtCore.QRect(340, 430, 51, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Controller)
        self.label_13.setGeometry(QtCore.QRect(340, 470, 51, 16))
        self.label_13.setObjectName("label_13")

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
        self.label_4.setText(_translate("Controller", "Possibility of anomaly generation"))
        self.label_5.setText(_translate("Controller", "Possibility of false positive"))
        self.label_6.setText(_translate("Controller", "Possibility of false negative"))
        self.label_11.setText(_translate("Controller", "%"))
        self.label_12.setText(_translate("Controller", "%"))
        self.label_13.setText(_translate("Controller", "%"))

    def decide_scenario(self):
        self.current_scenario = eval("scenario_data."+self.scenarios.currentText())
        if self.current_scenario['name'] == "None":
            self.map_list = []
            self.weather_list = []
            self.traffic_situ = []
            self.des_sce = "To launch the simulation,you have to at least select a scenario."
            self.des_map = ""
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_scenario['name'] == "scenario_1":
            self.map_list = scenario_data.map_normal
            self.weather_list = scenario_data.weather_fine
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_1
            self.des_map = scenario_data.map_info1
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_scenario['name'] == "scenario_2":
            self.map_list = scenario_data.map_normal
            self.weather_list = scenario_data.weather_fine
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_2
            self.des_map = scenario_data.map_info1
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_scenario['name'] == "scenario_3":
            self.map_list = scenario_data.map_highway
            self.weather_list = scenario_data.weather_fine
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_3
            self.des_map = scenario_data.map_info1
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)
        if self.current_scenario['name'] == "scenario_4":
            self.map_list = scenario_data.map_all
            self.weather_list = scenario_data.weather_bad
            self.traffic_situ = scenario_data.traffic_situations
            self.des_sce = scenario_data.description_4
            self.des_map = scenario_data.map_info1
            self.maps.clear()
            self.maps.addItems(self.map_list)
            self.weathers.clear()
            self.weathers.addItems(self.weather_list)
            self.situations.clear()
            self.situations.addItems(self.traffic_situ)
            self.descriptions.setText(self.des_sce+"\n\n"+self.des_map)

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
        if self.times.text() != "":
            self.simulation_time = int(self.times.text())
        if self.anomaly_possibility.text() != "":
            self.anomaly_pos = float(self.anomaly_possibility.text())
        if self.false_positive.text() != "":
            self.false_pos = float(self.false_positive.text())
        if self.false_negative.text() != "":
            self.false_neg = float(self.false_negative.text())
        if self.simulation_time > 20 or self.simulation_time < 3:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid simulation time.")
            msg.setText("The simulation time should be 3~20 mins.")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec()
        elif self.anomaly_pos < 0 or self.anomaly_pos > 100 or self.false_neg < 0 or self.false_neg > 100 or self.false_pos < 0 or self.false_pos > 100:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid possibility.")
            msg.setText("Possibility should be 0~100 %.")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec()
        else:
            print(self.current_scenario['name'],self.current_map,self.current_traffic,self.current_weather)
            print("time:",self.simulation_time,"anomaly:",self.anomaly_pos,"false positive:",self.false_pos,"false negative:",self.false_neg)
            generator.generate_scenario(self.current_scenario,self.current_map,self.current_weather,self.simulation_time,self.current_traffic,self.anomaly_pos,self.false_pos,self.false_neg)
            sys.exit()

    def leave(self):
        QApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    w = Ui_Controller()
    w.setupUi(mainwindow)

    mainwindow.show()
    sys.exit(app.exec_())
