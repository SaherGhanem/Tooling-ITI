# -*- coding: utf-8 -*-

################################################################################
## Author : Saher Ghanem
## INTAKE43
## GUI FOR GENERATE DIO_DRIVER_CONFIGRATION
## 12/10/2022
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


List = []
def newConfigs():
    global List
    List = []
    for port in range(0,4):
        Pins = []
        for pin in range(0,32):
            Pins.append([False, True, True, True, ''])
        List.append(Pins)
        
newConfigs()

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(936, 694)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 189, 243, 255), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox_29 = QGroupBox(Form)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setGeometry(QRect(230, 120, 631, 351))
        font = QFont()
        font.setFamily(u"Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_29.setFont(font)
        self.Output_Group = QGroupBox(self.groupBox_29)
        self.Output_Group.setObjectName(u"Output_Group")
        self.Output_Group.setGeometry(QRect(240, 39, 311, 81))
        self.Output_Group.setFont(font)
        self.High_OUTPUT = QRadioButton(self.Output_Group)
        self.High_OUTPUT.setObjectName(u"High_OUTPUT")
        self.High_OUTPUT.setGeometry(QRect(30, 40, 95, 20))
        self.High_OUTPUT.setChecked(True)
        self.LOW_OUTPUT = QRadioButton(self.Output_Group)
        self.LOW_OUTPUT.setObjectName(u"LOW_OUTPUT")
        self.LOW_OUTPUT.setGeometry(QRect(150, 40, 95, 20))
        self.LOW_OUTPUT.setChecked(False)
        self.IO_GROUP = QGroupBox(self.groupBox_29)
        self.IO_GROUP.setObjectName(u"IO_GROUP")
        self.IO_GROUP.setGeometry(QRect(10, 40, 211, 181))
        self.IO_GROUP.setFont(font)
        self.IO_GROUP.setMouseTracking(False)
        self.OUTPUT_IO = QRadioButton(self.IO_GROUP)
        self.OUTPUT_IO.setObjectName(u"OUTPUT_IO")
        self.OUTPUT_IO.setGeometry(QRect(10, 40, 121, 41))
        self.OUTPUT_IO.setChecked(True)
        self.INPUT_IO = QRadioButton(self.IO_GROUP)
        self.INPUT_IO.setObjectName(u"INPUT_IO")
        self.INPUT_IO.setGeometry(QRect(10, 120, 121, 31))
        self.INPUT_IO.setChecked(False)
        self.Input_Group = QGroupBox(self.groupBox_29)
        self.Input_Group.setObjectName(u"Input_Group")
        self.Input_Group.setEnabled(False)
        self.Input_Group.setGeometry(QRect(240, 140, 311, 80))
        self.Pull_Up = QRadioButton(self.Input_Group)
        self.Pull_Up.setObjectName(u"Pull_Up")
        self.Pull_Up.setGeometry(QRect(30, 30, 111, 20))
        self.Pull_Up.setFont(font)
        self.Pull_Up.setChecked(True)
        self.High_Imp = QRadioButton(self.Input_Group)
        self.High_Imp.setObjectName(u"High_Imp")
        self.High_Imp.setGeometry(QRect(150, 30, 131, 20))
        self.label = QLabel(self.groupBox_29)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 250, 111, 21))
        self.LINE_PIN_Name = QLineEdit(self.groupBox_29)
        self.LINE_PIN_Name.setObjectName(u"LINE_PIN_Name")
        self.LINE_PIN_Name.setGeometry(QRect(30, 280, 211, 41))
        self.Default_name = QCheckBox(self.groupBox_29)
        self.Default_name.setObjectName(u"Default_name")
        self.Default_name.setGeometry(QRect(300, 290, 181, 31))
        self.PATH_LINE = QLineEdit(Form)
        self.PATH_LINE.setObjectName(u"PATH_LINE")
        self.PATH_LINE.setGeometry(QRect(230, 490, 471, 51))
        self.PATH_LINE.setFont(font)
        self.Generate_PUSHBUTTON = QPushButton(Form)
        self.Generate_PUSHBUTTON.setObjectName(u"Generate_PUSHBUTTON")
        self.Generate_PUSHBUTTON.setGeometry(QRect(710, 490, 151, 51))
        self.Generate_PUSHBUTTON.setFont(font)
        self.PORT_NAME = QComboBox(Form)
        self.PORT_NAME.addItem(str())
        self.PORT_NAME.addItem(str())
        self.PORT_NAME.addItem(str())
        self.PORT_NAME.addItem(str())
        self.PORT_NAME.setObjectName(u"PORT_NAME")
        self.PORT_NAME.setGeometry(QRect(40, 200, 171, 41))
        font1 = QFont()
        font1.setFamily(u"Rockwell")
        font1.setPointSize(18)
        self.PORT_NAME.setFont(font1)
        self.PIN_NAME = QComboBox(Form)
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.addItem(str())
        self.PIN_NAME.setObjectName(u"PIN_NAME")
        self.PIN_NAME.setGeometry(QRect(60, 350, 111, 41))
        self.PIN_NAME.setFont(font1)
        self.PIN_NAME.setLayoutDirection(Qt.LeftToRight)
        self.SAVE_PUSHBUTTON = QPushButton(Form)
        self.SAVE_PUSHBUTTON.setObjectName(u"SAVE_PUSHBUTTON")
        self.SAVE_PUSHBUTTON.setGeometry(QRect(570, 580, 151, 51))
        self.SAVE_PUSHBUTTON.setFont(font)
        self.LOAD_PUSHBUTTON = QPushButton(Form)
        self.LOAD_PUSHBUTTON.setObjectName(u"LOAD_PUSHBUTTON")
        self.LOAD_PUSHBUTTON.setGeometry(QRect(310, 580, 151, 51))
        self.LOAD_PUSHBUTTON.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 10, 341, 41))
        font2 = QFont()
        font2.setFamily(u"Rockwell")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 60, 201, 41))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(460, 30, 281, 41))
        self.label_5.setFont(font2)
        self.groupBox_29.raise_()
        self.Generate_PUSHBUTTON.raise_()
        self.PATH_LINE.raise_()
        self.PORT_NAME.raise_()
        self.PIN_NAME.raise_()
        self.SAVE_PUSHBUTTON.raise_()
        self.LOAD_PUSHBUTTON.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Form)
        self.OUTPUT_IO.toggled.connect(self.Output_Group.setEnabled)
        self.OUTPUT_IO.toggled.connect(self.Input_Group.setDisabled)
        self.INPUT_IO.toggled.connect(self.Output_Group.setDisabled)
        self.INPUT_IO.toggled.connect(self.Input_Group.setEnabled)
        
        self.Generate_PUSHBUTTON.clicked.connect(self.gen)
        
        self.Default_name.toggled.connect(self.LINE_PIN_Name.setDisabled)
        
        self.PORT_NAME.currentIndexChanged.connect(self.PPChange)
        self.PIN_NAME.currentIndexChanged.connect(self.PPChange)
        
        
        self.OUTPUT_IO.toggled.connect      (self.change)
        self.High_OUTPUT.toggled.connect    (self.change)
        self.Pull_Up.toggled.connect        (self.change)
        self.PATH_LINE.textChanged.connect  (self.change)
        #self.LINE_PIN_Name.toggled.connect  (self.change)

        
        self.SAVE_PUSHBUTTON.clicked.connect(self.save)
        self.LOAD_PUSHBUTTON.clicked.connect(self.load)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def gen(self):
      path= self.PATH_LINE.text()
      
      if path != '':
        file = open(path+'\PORT_Config.h','w')
      else: 
        file = open('PORT_Config.h','w')
             
      file.write('#ifndef\tDIO_CONFIG_H\n#define\tDIO_CONFIG_H\n\n')
      file.write('#define\tHIGH\t\t1\n')
      file.write('#define\tLOW\t\t0\n')
      file.write('#define\tHIGH_IMPEDANCE\t\t0\n')
      file.write('#define\tPULL_UP\t\t1\n')
      file.write('#define\tOUTPUT\t\t1\n')
      file.write('#define\tINPUT\t\t0\n\n\n')
      letters = ['A','B','C','D']
      direction = ''
      value = ''
      for i in range(0,4):
          for j in range(0,8):
              if List[i][j][0] == True:  
                  direction = 'OUTPUT'
                  if List[i][j][1] == True:    
                      value = 'High'
                  else:
                      value = 'LOW'
              else:
                  direction = 'INPUT'
                  if List[i][j][2] == True:      
                      value = 'HIGH_IMPEDANCE'
                  else:
                      value = 'PULL_UP'
                      
              if List[i][j][3] == True:         
                  file.write('#define\tPORT'+letters[i]+'_PIN'+ str(j) + '_DIR\t\t'+direction+'\n')  
                  file.write('#define\tPORT'+letters[i]+'_PIN'+ str(j) + '_VAL\t\t'+value+'\n\n')
              else:
                  file.write('#define\tPORT'+letters[i]+'_'+ List[i][j][4] + '_DIR\t\t'+direction+'\n')
                  file.write('#define\tPORT'+letters[i]+'_'+ List[i][j][4] + '_VAL\t\t'+value+'\n\n')
      file.write('\n#endif')
    def change(self):
           pin  = self.PIN_NAME.currentIndex()
           port = self.PORT_NAME.currentIndex()
           List[port][pin][0] = self.OUTPUT_IO.isChecked()
           List[port][pin][1] = self.High_OUTPUT.isChecked()
           List[port][pin][2] = self.Pull_Up.isChecked()
           List[port][pin][3] = self.Default_name.isChecked()
           List[port][pin][4] = self.LINE_PIN_Name.text()
           

    def save(self):
        file = open('testSave.bin','w')
        for i in range(0,4):
            for j in range(0,8):
                for k in range(0,5):
                    file.write(str(List[i][j][k])+'\n')
        file.close()




    def load(self):
        file = open('testSave.bin','r')
        for i in range(0,4):
            for j in range(0,8):
                List[i][j][0] = Bool(file.readline().strip())
                List[i][j][1] = Bool(file.readline().strip())
                List[i][j][2] = Bool(file.readline().strip())
                List[i][j][3] = Bool(file.readline().strip())
                List[i][j][4] = file.readline().strip()
        file.close()
        self.PPChange()
  

    def PPChange(self):
        self.OUTPUT_IO.toggled.disconnect(self.change)
        self.High_OUTPUT.toggled.disconnect(self.change)
        self.Pull_Up.toggled.disconnect(self.change)
     #   self.LINE_PIN_Name.textChanged.disconnect(self.change)
       # self.Default_name.toggled.disconnect(self.change)

        pin = self.PIN_NAME.currentIndex()
        port = self.PORT_NAME.currentIndex()
        self.OUTPUT_IO.setChecked(List[port][pin][0])
        self.INPUT_IO.setChecked(not List[port][pin][0])
        self.High_OUTPUT.setChecked(List[port][pin][1])
        self.LOW_OUTPUT.setChecked(not List[port][pin][1])
        self.High_Imp.setChecked(List[port][pin][2])
        self.Pull_Up.setChecked(not List[port][pin][2])
        self.Default_name.setChecked(List[port][pin][3])
        self.LINE_PIN_Name.setEnabled(not List[port][pin][3])
        self.LINE_PIN_Name.setText(List[port][pin][4])

        self.OUTPUT_IO.toggled.connect(self.change)
        self.High_OUTPUT.toggled.connect(self.change)
        self.Pull_Up.toggled.connect(self.change)
        self.LINE_PIN_Name.textChanged.connect(self.change)
        self.Default_name.toggled.connect(self.change)
     
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.Output_Group.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_OUTPUT.setText(QCoreApplication.translate("Form", u"High", None))
        self.LOW_OUTPUT.setText(QCoreApplication.translate("Form", u"Low", None))
        self.IO_GROUP.setTitle(QCoreApplication.translate("Form", u"I/O", None))
        self.OUTPUT_IO.setText(QCoreApplication.translate("Form", u"Output", None))
        self.INPUT_IO.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp.setText(QCoreApplication.translate("Form", u"High_Imp", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pin_Name", None))
        self.LINE_PIN_Name.setText("")
        self.LINE_PIN_Name.setPlaceholderText(QCoreApplication.translate("Form", u"Enter PIN Name", None))
        self.Default_name.setText(QCoreApplication.translate("Form", u"Default_name", None))
        self.PATH_LINE.setPlaceholderText(QCoreApplication.translate("Form", u"Please Enter The Path", None))
        self.Generate_PUSHBUTTON.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.PORT_NAME.setItemText(0, QCoreApplication.translate("Form", u"POART_A", None))
        self.PORT_NAME.setItemText(1, QCoreApplication.translate("Form", u"POART_B", None))
        self.PORT_NAME.setItemText(2, QCoreApplication.translate("Form", u"POART_C", None))
        self.PORT_NAME.setItemText(3, QCoreApplication.translate("Form", u"POART_D", None))

        self.PIN_NAME.setItemText(0, QCoreApplication.translate("Form", u"PIN_0", None))
        self.PIN_NAME.setItemText(1, QCoreApplication.translate("Form", u"PIN_1", None))
        self.PIN_NAME.setItemText(2, QCoreApplication.translate("Form", u"PIN_2", None))
        self.PIN_NAME.setItemText(3, QCoreApplication.translate("Form", u"PIN_3", None))
        self.PIN_NAME.setItemText(4, QCoreApplication.translate("Form", u"PIN_4", None))
        self.PIN_NAME.setItemText(5, QCoreApplication.translate("Form", u"PIN_5", None))
        self.PIN_NAME.setItemText(6, QCoreApplication.translate("Form", u"PIN_6", None))
        self.PIN_NAME.setItemText(7, QCoreApplication.translate("Form", u"PIN_7", None))

        self.SAVE_PUSHBUTTON.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.LOAD_PUSHBUTTON.setText(QCoreApplication.translate("Form", u"LOAD", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Created by: SAHER GHANEM", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ITI INTAKE-43", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"DIO_CONFIGURATION", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Widget=QWidget()
    Form=Ui_Form()
    Form.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
    
