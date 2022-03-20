from PyQt5 import QtCore, QtGui, QtWidgets
import time,json,os,base64
def decodepw(before,pwkey):
    try:
        s1,after='',''
        for s in before:
            after=after+str(chr(ord(s)+pwkey))+'\U0010f2c3'
        after=base64.b64encode(after.encode('utf-8')).decode('utf-8')
        return after
    except ValueError:
        if ord(s)+pwkey>1114111 or ord(s)+pwkey<0:
            return 'ValueError:String and keys are out of range, try reducing the number of keys'
def encodepw(before,pwkey):
    try:
        l1,after,s2=[],'',''
        s2=base64.b64decode(before.encode('utf-8')).decode('utf-8')
        for s in s2:
            if s=='\U0010f2c3':
                l1.append(after)
                after=''
            else:
                after=after+s
        for l in l1:
                after=after+str(chr(ord(l)-pwkey))
        return after
    except ValueError:
        if ord(l)-pwkey>1114111 or ord(l)-pwkey<0:
            return 'ValueError:String and keys are out of range, try reducing the number of keys'
class Ui_fristSet(object):
    def setupUi(self, fristSet):
        fristSet.setObjectName("fristSet")
        fristSet.resize(490, 266)
        fristSet.setMinimumSize(QtCore.QSize(490, 266))
        fristSet.setMaximumSize(QtCore.QSize(490, 266))
        fristSet.setWindowOpacity(0.95)
        fristSet.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        fristSet.setOptions(QtWidgets.QWizard.HelpButtonOnRight|QtWidgets.QWizard.NoCancelButton)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setGeometry(QtCore.QRect(60, 70, 381, 18))
        self.label.setText("检测到您是初次使用，请在此设置必要参数")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 331, 61))
        self.label_2.setText("It is detected that you are using it \nfor the first time, please set the \nnecessary parameters here")
        self.label_2.setObjectName("label_2")
        fristSet.addPage(self.wizardPage1)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.label_3 = QtWidgets.QLabel(self.wizardPage2)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 81, 18))
        self.label_3.setText("语言")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.wizardPage2)
        self.label_4.setGeometry(QtCore.QRect(50, 80, 101, 18))
        self.label_4.setText("Language")
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.wizardPage2)
        self.checkBox.setGeometry(QtCore.QRect(200, 70, 99, 22))
        self.checkBox.setText("中文")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.wizardPage2)
        self.checkBox_2.setGeometry(QtCore.QRect(320, 70, 99, 22))
        self.checkBox_2.setText("English")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_5 = QtWidgets.QLabel(self.wizardPage2)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 81, 18))
        self.label_5.setText("密码")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.wizardPage2)
        self.label_6.setGeometry(QtCore.QRect(50, 160, 81, 18))
        self.label_6.setText("Password")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.wizardPage2)
        self.lineEdit.setGeometry(QtCore.QRect(180, 140, 231, 25))
        self.lineEdit.setInputMask("")
        self.lineEdit.setMaxLength(14)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        fristSet.addPage(self.wizardPage2)
        self.retranslateUi(fristSet)
        self.checkBox.clicked.connect(self.checkBox_2.toggle)
        self.checkBox_2.clicked.connect(self.checkBox.toggle)
        self.lineEdit.editingFinished.connect(saveconfig)
        QtCore.QMetaObject.connectSlotsByName(fristSet)
    def retranslateUi(self, fristSet):
        _translate = QtCore.QCoreApplication.translate
        fristSet.setWindowTitle(_translate("fristSet", "初次使用/first time"))
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(514, 475)
        mainWindow.setMinimumSize(QtCore.QSize(514, 475))
        mainWindow.setMaximumSize(QtCore.QSize(896, 765))
        font = QtGui.QFont()
        font.setPointSize(9)
        mainWindow.setFont(font)
        mainWindow.setWindowOpacity(0.95)
        mainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.settingButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.settingButton.setFont(font)
        self.settingButton.setObjectName("settingButton")
        self.gridLayout.addWidget(self.settingButton, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 2, 2, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(256, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setMouseTracking(False)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.clear()
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(mainWindow)
        self.saveButton.clicked.connect(savethink)
        self.settingButton.clicked.connect(setting)
        self.pushButton.clicked.connect(manage)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "主窗口"))
        self.settingButton.setText(_translate("mainWindow", "设置"))
        self.pushButton.setText(_translate("mainWindow", "管理"))
        self.saveButton.setText(_translate("mainWindow", "保存"))
        self.plainTextEdit.setPlaceholderText(_translate("mainWindow", "输入你的想法。"))
    def retranslateUi_eng(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Main window"))
        self.settingButton.setText(_translate("mainWindow", "Setting"))
        self.pushButton.setText(_translate("mainWindow", "Manage"))
        self.saveButton.setText(_translate("mainWindow", "Save"))
        self.plainTextEdit.setPlaceholderText(_translate("mainWindow", "Enter your thoughts."))
class Ui_settingsForm(object):
    def setupUi(self, settingsForm):
        settingsForm.setObjectName("settingsForm")
        settingsForm.resize(683, 578)
        settingsForm.setMinimumSize(QtCore.QSize(683, 578))
        settingsForm.setMaximumSize(QtCore.QSize(683, 578))
        settingsForm.setWindowOpacity(0.95)
        self.gridLayout = QtWidgets.QGridLayout(settingsForm)
        self.gridLayout.setObjectName("gridLayout")
        self.saveandcloseButton = QtWidgets.QPushButton(settingsForm)
        self.saveandcloseButton.setObjectName("saveandcloseButton")
        self.gridLayout.addWidget(self.saveandcloseButton, 1, 1, 1, 1)
        self.aboutButton = QtWidgets.QPushButton(settingsForm)
        self.aboutButton.setObjectName("aboutButton")
        self.gridLayout.addWidget(self.aboutButton, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(settingsForm)
        self.tabWidget.setMinimumSize(QtCore.QSize(661, 511))
        self.tabWidget.setMaximumSize(QtCore.QSize(661, 511))
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.saveBox = QtWidgets.QGroupBox(self.mainTab)
        self.saveBox.setGeometry(QtCore.QRect(20, 10, 621, 191))
        self.saveBox.setObjectName("saveBox")
        self.saveFiletipjson = QtWidgets.QLabel(self.saveBox)
        self.saveFiletipjson.setGeometry(QtCore.QRect(20, 20, 221, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.saveFiletipjson.setPalette(palette)
        self.saveFiletipjson.setObjectName("saveFiletipjson")
        self.choosesaveFileButton = QtWidgets.QPushButton(self.saveBox)
        self.choosesaveFileButton.setGeometry(QtCore.QRect(250, 30, 151, 51))
        self.choosesaveFileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choosesaveFileButton.setObjectName("choosesaveFileButton")
        self.groupBox = QtWidgets.QGroupBox(self.mainTab)
        self.groupBox.setGeometry(QtCore.QRect(20, 220, 621, 191))
        self.groupBox.setObjectName("groupBox")
        self.setpasswordButton = QtWidgets.QPushButton(self.groupBox)
        self.setpasswordButton.setGeometry(QtCore.QRect(230, 30, 151, 61))
        self.setpasswordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setpasswordButton.setObjectName("setpasswordButton")
        self.setpasswordButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.setpasswordButton_2.setGeometry(QtCore.QRect(230, 100, 151, 61))
        self.setpasswordButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setpasswordButton_2.setObjectName("setpasswordButton")
        self.setpasswordButton_2.setDisabled(True)
        self.tabWidget.addTab(self.mainTab, "")
        self.otherTab = QtWidgets.QWidget()
        self.otherTab.setObjectName("otherTab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.otherTab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 621, 451))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(340, 20, 256, 391))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 201, 25))
        self.lineEdit.setStatusTip("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(20)
        self.addButton = QtWidgets.QPushButton(self.groupBox_2)
        self.addButton.setGeometry(QtCore.QRect(230, 50, 99, 28))
        self.addButton.setObjectName("addButton")
        self.delButton = QtWidgets.QPushButton(self.groupBox_2)
        self.delButton.setGeometry(QtCore.QRect(200, 370, 99, 28))
        self.delButton.setCheckable(False)
        self.delButton.setChecked(False)
        self.delButton.setObjectName("delButton")
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette1 = QtGui.QPalette()
        palette1.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.classtip = QtWidgets.QLabel(self.groupBox_2)
        self.classtip.setObjectName("classtip")
        self.classtip.setText("")
        self.classtip.setPalette(palette1)
        self.classtip.setGeometry(QtCore.QRect(60, 120, 241, 151))
        self.classtip.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.tabWidget.addTab(self.otherTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.retranslateUi(settingsForm)
        self.aboutButton.clicked.connect(lambda:aboutWindow.show())
        self.addButton.clicked.connect(addclass)
        self.lineEdit.textChanged.connect(inputclass)
        self.tabWidget.setCurrentIndex(0)
        self.saveandcloseButton.clicked.connect(save)
        self.setpasswordButton.clicked.connect(setpassword)
        self.setpasswordButton_2.clicked.connect(setpw)
        self.delButton.clicked.connect(delclass)
        self.choosesaveFileButton.clicked.connect(choosesaveFile)
        QtCore.QMetaObject.connectSlotsByName(settingsForm)
    def retranslateUi(self, settingsForm):
        _translate = QtCore.QCoreApplication.translate
        settingsForm.setWindowTitle(_translate("settingsForm", "设置"))
        self.saveandcloseButton.setText(_translate("settingsForm", "确定"))
        self.aboutButton.setText(_translate("settingsForm", "关于"))
        self.saveBox.setTitle(_translate("settingsForm", "保存"))
        self.saveFiletipjson.setText(_translate("settingsForm", "建议更换保存路径！"))
        self.choosesaveFileButton.setText(_translate("settingsForm", "选择保存路径"))
        self.groupBox.setTitle(_translate("settingsForm", "安全"))
        self.setpasswordButton.setText(_translate("settingsForm", "更改密码"))
        self.setpasswordButton_2.setText(_translate("settingsForm", "更改密钥\n(谨慎操作)"))
        self.setpasswordButton_2.setToolTip(_translate("settingForm", "此按钮暂时不可用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("settingsForm", "通用"))
        self.groupBox_2.setTitle(_translate("settingsForm", "分类"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setPlaceholderText(_translate("settingsForm", "输入你想添加的类"))
        self.addButton.setText(_translate("settingsForm", "加入"))
        self.delButton.setText(_translate("settingsForm", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.otherTab), _translate("settingsForm", "其他"))
    def retranslateUi_eng(self, settingsForm):
        _translate = QtCore.QCoreApplication.translate
        settingsForm.setWindowTitle(_translate("settingsForm", "Setting"))
        self.saveandcloseButton.setText(_translate("settingsForm", "Sure"))
        self.aboutButton.setText(_translate("settingsForm", "About"))
        self.saveBox.setTitle(_translate("settingsForm", "Save"))
        self.saveFiletipjson.setText(_translate("settingsForm", "It is recommended to \nchange the save path!"))
        self.choosesaveFileButton.setText(_translate("settingsForm", "Choose a \nsave path"))
        self.groupBox.setTitle(_translate("settingsForm", "Safety"))
        self.setpasswordButton.setText(_translate("settingsForm", "Change the\n password"))
        self.setpasswordButton_2.setText(_translate("settingsForm", "Change key\n(use caution)"))
        self.setpasswordButton_2.setToolTip(_translate("settingForm", "This button is temporarily unavailable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("settingsForm", "Universal"))
        self.groupBox_2.setTitle(_translate("settingsForm", "Classification"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setPlaceholderText(_translate("settingsForm", "Enter the class you want to add"))
        self.addButton.setText(_translate("settingsForm", "Add"))
        self.delButton.setText(_translate("settingsForm", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.otherTab), _translate("settingsForm", "Other"))
class Ui_setpasswordDialog(object):
    def setupUi(self, setpasswordDialog):
        setpasswordDialog.setObjectName("setpasswordDialog")
        setpasswordDialog.resize(464, 307)
        setpasswordDialog.setMinimumSize(QtCore.QSize(464, 274))
        setpasswordDialog.setMaximumSize(QtCore.QSize(737, 505))
        setpasswordDialog.setWindowOpacity(0.95)
        setpasswordDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gridLayout = QtWidgets.QGridLayout(setpasswordDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(setpasswordDialog)
        self.lineEdit_2.setMaxLength(14)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(setpasswordDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(setpasswordDialog)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(14)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(setpasswordDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(setpasswordDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.tip = QtWidgets.QLabel(setpasswordDialog)
        self.tip.setObjectName("tip")
        self.gridLayout.addWidget(self.tip, 4, 0, 1, 1)
        self.retranslateUi(setpasswordDialog)
        self.buttonBox.accepted.connect(setpasswordDialog.accept)
        self.buttonBox.rejected.connect(setpasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(setpasswordDialog)
    def retranslateUi(self, setpasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        setpasswordDialog.setWindowTitle(_translate("setpasswordDialog", "设置密码"))
        self.label_2.setText(_translate("setpasswordDialog", "输入新密码"))
        self.label_3.setText(_translate("setpasswordDialog", "重复输入新密码"))
        self.tip.setText(_translate("setpasswordDialog", " "))
    def retranslateUi_eng(self, setpasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        setpasswordDialog.setWindowTitle(_translate("setpasswordDialog", "Set password"))
        self.label_2.setText(_translate("setpasswordDialog", "Enter a new password"))
        self.label_3.setText(_translate("setpasswordDialog", "Enter new password repeatedly"))
        self.tip.setText(_translate("setpasswordDialog", " "))
    def retranslateUi_pw(self, setpasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        setpasswordDialog.setWindowTitle(_translate("setpasswordDialog", "设置密钥"))
        self.label_2.setText(_translate("setpasswordDialog", "输入新密钥"))
        self.label_3.setText(_translate("setpasswordDialog", "重复输入新密钥"))
        self.tip.setText(_translate("setpasswordDialog", " "))
    def retranslateUi_pw_eng(self, setpasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        setpasswordDialog.setWindowTitle(_translate("setpasswordDialog", "Set key"))
        self.label_2.setText(_translate("setpasswordDialog", "Enter new key"))
        self.label_3.setText(_translate("setpasswordDialog", "Enter new key repeatedly"))
        self.tip.setText(_translate("setpasswordDialog", " "))
class Ui_aboutForm(object):
    def setupUi(self, aboutForm):
        aboutForm.setObjectName("aboutForm")
        aboutForm.resize(502, 327)
        aboutForm.setMinimumSize(QtCore.QSize(502, 327))
        aboutForm.setMaximumSize(QtCore.QSize(502, 327))
        aboutForm.setWindowOpacity(0.95)
        aboutForm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton = QtWidgets.QPushButton(aboutForm)
        self.pushButton.setGeometry(QtCore.QRect(410, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(aboutForm)
        self.textBrowser.setGeometry(QtCore.QRect(40, 30, 421, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(aboutForm)
        self.pushButton.clicked.connect(aboutForm.close)
        QtCore.QMetaObject.connectSlotsByName(aboutForm)
    def retranslateUi(self, aboutForm):
        _translate = QtCore.QCoreApplication.translate
        aboutForm.setWindowTitle(_translate("aboutForm", "关于"))
        self.pushButton.setText(_translate("aboutForm", "关闭"))
        self.textBrowser.setMarkdown(_translate("aboutForm", "克服重重困难，这个程序终于完工了，心里还是很高兴的。源代码会传到Github，首次实现中英双语应该值得开心一下(虽然几乎全部是用Google翻的)。<br></br>希望大家能提出建议！<br></br>2022.2.8<br></br>link<br></br><br></br>\n\nAfter overcoming many difficulties, this program is finally completed, and I am still very happy. The source code will be uploaded to Github, and it should be fun to implement Chinese and English bilingualism for the first time (although almost all of them are translated by Google). <br></br>I hope you can make suggestions! <br></br>2022.2.8<br></br>link<br></br>translate by Google\n\n"))
    def retranslateUi_eng(self, aboutForm):
        _translate = QtCore.QCoreApplication.translate
        aboutForm.setWindowTitle(_translate("aboutForm", "About"))
        self.pushButton.setText(_translate("aboutForm", "Close"))
        self.textBrowser.setMarkdown(_translate("aboutForm", "克服重重困难，这个程序终于完工了，心里还是很高兴的。源代码会传到Github，首次实现中英双语应该值得开心一下(虽然几乎全部是用Google翻的)。<br></br>希望大家能提出建议！<br></br>2022.2.8<br></br>link<br></br><br></br>\n\nAfter overcoming many difficulties, this program is finally completed, and I am still very happy. The source code will be uploaded to Github, and it should be fun to implement Chinese and English bilingualism for the first time (although almost all of them are translated by Google). <br></br>I hope you can make suggestions! <br></br>2022.2.8<br></br>link<br></br>translate by Google\n\n"))
class Ui_inpwForm(object):
    def setupUi(self, inpwForm):
        inpwForm.setObjectName("inpwForm")
        inpwForm.resize(582, 151)
        inpwForm.setMinimumSize(QtCore.QSize(499, 50))
        inpwForm.setMaximumSize(QtCore.QSize(582, 151))
        inpwForm.setWindowOpacity(0.95)
        inpwForm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.horizontalLayout = QtWidgets.QHBoxLayout(inpwForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(inpwForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(inpwForm)
        self.lineEdit.setMaxLength(14)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(inpwForm)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit.textChanged.connect(fuyuan)
        self.retranslateUi(inpwForm)
        QtCore.QMetaObject.connectSlotsByName(inpwForm)
    def retranslateUi(self, inpwForm):
        _translate = QtCore.QCoreApplication.translate
        inpwForm.setWindowTitle(_translate("inpwForm", "请输入密码"))
        self.label.setText(_translate("inpwForm", "请输入密码："))
        self.lineEdit.setToolTip(_translate("inpwForm", "在这里输入密码"))
        self.lineEdit.setPlaceholderText(_translate("inpwForm", "在这里输入密码"))
        self.pushButton.setText(_translate("inpwForm", "继续"))
    def retranslateUi_eng(self, inpwForm):
        _translate = QtCore.QCoreApplication.translate
        inpwForm.setWindowTitle(_translate("inpwForm", "Please enter password"))
        self.label.setText(_translate("inpwForm", "Please enter the password:"))
        self.lineEdit.setToolTip(_translate("inpwForm", "Enter password here"))
        self.lineEdit.setPlaceholderText(_translate("inpwForm", "Enter password here"))
        self.pushButton.setText(_translate("inpwForm", "Next"))
class Ui_manageForm(object):
    def setupUi(self, manageForm):
        manageForm.setObjectName("manageForm")
        manageForm.resize(806, 580)
        manageForm.setMinimumSize(QtCore.QSize(806, 580))
        manageForm.setMaximumSize(QtCore.QSize(806, 580))
        manageForm.setWindowOpacity(0.95)
        manageForm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.tabWidget = QtWidgets.QTabWidget(manageForm)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 771, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(140, 70, 421, 71))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 0, 731, 501))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setGeometry(QtCore.QRect(110,30, 441, 101))
        self.label_2.setObjectName("label_2")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton = QtWidgets.QPushButton(self.tab_6)
        self.pushButton.setGeometry(QtCore.QRect(290, 10, 99, 28))
        self.pushButton.setObjectName("pushButton")
        self.allfinder = QtWidgets.QTextBrowser(self.tab_6)
        self.allfinder.setGeometry(QtCore.QRect(50, 60, 601, 331))
        self.allfinder.setObjectName("allfinder")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_7)
        self.tabWidget_3.setGeometry(QtCore.QRect(20, 0, 691, 461))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_8)
        self.tabWidget_4.setGeometry(QtCore.QRect(10, 0, 671, 441))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 271, 25))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.findButton = QtWidgets.QPushButton(self.tab_10)
        self.findButton.setGeometry(QtCore.QRect(420, 10, 99, 28))
        self.findButton.setObjectName("findButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 50, 271, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.findButton_2 = QtWidgets.QPushButton(self.tab_10)
        self.findButton_2.setGeometry(QtCore.QRect(420, 50, 99, 28))
        self.findButton_2.setObjectName("findButton_2")
        self.timefinder = QtWidgets.QTextBrowser(self.tab_10)
        self.timefinder.setGeometry(QtCore.QRect(50, 90, 561, 281))
        self.timefinder.setObjectName("timefinder")
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.yspinBox = QtWidgets.QSpinBox(self.tab_11)
        self.yspinBox.setGeometry(QtCore.QRect(18, 30, 71, 24))
        self.yspinBox.setMinimum(1970)
        self.yspinBox.setMaximum(2038)
        self.yspinBox.setProperty("value", 2022)
        self.yspinBox.setObjectName("yspinBox")
        self.mspinBox_2 = QtWidgets.QSpinBox(self.tab_11)
        self.mspinBox_2.setGeometry(QtCore.QRect(136, 30, 49, 24))
        self.mspinBox_2.setMinimum(1)
        self.mspinBox_2.setMaximum(12)
        self.mspinBox_2.setProperty("value", 2)
        self.mspinBox_2.setObjectName("mspinBox_2")
        self.dspinBox_3 = QtWidgets.QSpinBox(self.tab_11)
        self.dspinBox_3.setGeometry(QtCore.QRect(245, 30, 49, 24))
        self.dspinBox_3.setMinimum(1)
        self.dspinBox_3.setMaximum(31)
        self.dspinBox_3.setSingleStep(1)
        self.dspinBox_3.setProperty("value", 8)
        self.dspinBox_3.setObjectName("dspinBox_3")
        self.hspinBox_4 = QtWidgets.QSpinBox(self.tab_11)
        self.hspinBox_4.setGeometry(QtCore.QRect(353, 30, 49, 24))
        self.hspinBox_4.setMinimum(0)
        self.hspinBox_4.setMaximum(23)
        self.hspinBox_4.setProperty("value", 10)
        self.hspinBox_4.setObjectName("hspinBox_4")
        self.mspinBox_5 = QtWidgets.QSpinBox(self.tab_11)
        self.mspinBox_5.setGeometry(QtCore.QRect(461, 30, 49, 24))
        self.mspinBox_5.setMaximum(59)
        self.mspinBox_5.setProperty("value", 23)
        self.mspinBox_5.setObjectName("mspinBox_5")
        self.sspinBox_6 = QtWidgets.QSpinBox(self.tab_11)
        self.sspinBox_6.setGeometry(QtCore.QRect(570, 30, 49, 24))
        self.sspinBox_6.setMaximum(59)
        self.sspinBox_6.setSingleStep(1)
        self.sspinBox_6.setProperty("value", 23)
        self.sspinBox_6.setObjectName("sspinBox_6")
        self.label_3 = QtWidgets.QLabel(self.tab_11)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 561, 18))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.tab_11)
        self.checkBox.setGeometry(QtCore.QRect(20, 60, 99, 22))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_11)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 90, 99, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 80, 99, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.timefinder_2 = QtWidgets.QTextBrowser(self.tab_11)
        self.timefinder_2.setGeometry(QtCore.QRect(10, 120, 651, 281))
        self.timefinder_2.setObjectName("timefinder_2")
        self.label_3.raise_()
        self.yspinBox.raise_()
        self.mspinBox_2.raise_()
        self.dspinBox_3.raise_()
        self.hspinBox_4.raise_()
        self.mspinBox_5.raise_()
        self.sspinBox_6.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.pushButton_2.raise_()
        self.timefinder_2.raise_()
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.comboBox = QtWidgets.QComboBox(self.tab_9)
        self.comboBox.setGeometry(QtCore.QRect(70, 20, 171, 24))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 20, 99, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.classfinder = QtWidgets.QTextBrowser(self.tab_9)
        self.classfinder.setGeometry(QtCore.QRect(20, 70, 631, 341))
        self.classfinder.setObjectName("classfinder")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 230, 99, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.cleartip = QtWidgets.QLabel(self.tab_3)
        self.cleartip.setGeometry(QtCore.QRect(110, 190, 81, 18))
        self.cleartip.setObjectName("cleartip")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 30, 99, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.outputtip = QtWidgets.QLabel(self.tab_4)
        self.outputtip.setGeometry(QtCore.QRect(20, 20, 211, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.outputtip.setPalette(palette)
        self.outputtip.setObjectName("outputtip")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 110, 99, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_4, "")
        self.retranslateUi(manageForm)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.checkBox.clicked.connect(self.checkBox_2.toggle)
        self.checkBox_2.clicked.connect(self.checkBox.toggle)
        self.pushButton_5.clicked.connect(choosesaveFile_ma)
        self.pushButton_6.clicked.connect(daochu)
        self.pushButton.clicked.connect(readohhh)
        self.findButton.clicked.connect(readohhhh)
        self.findButton_2.clicked.connect(readohhhhh)
        self.pushButton_3.clicked.connect(findbyclass)
        self.pushButton_2.clicked.connect(findbytime)
        self.pushButton_4.clicked.connect(clearly)
        QtCore.QMetaObject.connectSlotsByName(manageForm)
    def retranslateUi(self, manageForm):
        _translate = QtCore.QCoreApplication.translate
        manageForm.setWindowTitle(_translate("manageForm", "管理"))
        self.label.setText(_translate("manageForm", "这里是首页\n你可以通过上方选项卡的切换实现不同的管理功能"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("manageForm", "首页"))
        self.label_2.setText(_translate("manageForm", "你可以通过选择上方标签来实现不同功能"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("manageForm", "首先"))
        self.pushButton.setText(_translate("manageForm", "开始"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("manageForm", "全文阅读"))
        self.lineEdit.setPlaceholderText(_translate("manageForm", "在这里输入时间戳(精确到秒)"))
        self.findButton.setText(_translate("manageForm", "查找"))
        self.lineEdit_2.setPlaceholderText(_translate("manageForm", "或在这里输入格式化后的时间"))
        self.findButton_2.setText(_translate("manageForm", "查找"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("manageForm", "按时间戳选"))
        self.label_3.setText(_translate("manageForm", "年           月          日          时          分         秒"))
        self.checkBox.setText(_translate("manageForm", "或"))
        self.checkBox_2.setText(_translate("manageForm", "与"))
        self.pushButton_2.setText(_translate("manageForm", "查找"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("manageForm", "按时间元组选"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("manageForm", "按时间选"))
        self.pushButton_3.setText(_translate("manageForm", "查找"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("manageForm", "按类别选"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("manageForm", "选择阅读"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("manageForm", "阅读"))
        self.pushButton_4.setText(_translate("manageForm", "清空"))
        self.cleartip.setText(_translate("manageForm", " "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("manageForm", "清空"))
        self.pushButton_5.setText(_translate("manageForm", "选择路径"))
        self.outputtip.setText(_translate("manageForm", "请选择路径！"))
        self.pushButton_6.setText(_translate("manageForm", "导出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("manageForm", "导出"))
    def retranslateUi_eng(self, manageForm):
        _translate = QtCore.QCoreApplication.translate
        manageForm.setWindowTitle(_translate("manageForm", "Manage"))
        self.label.setText(_translate("manageForm", "This is the home page\nYou can achieve different management functions by switching the upper tabs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("manageForm", "Front page"))
        self.label_2.setText(_translate("manageForm", "You can achieve different functions by selecting the tab above"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("manageForm", "Firstly"))
        self.pushButton.setText(_translate("manageForm", "Start"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("manageForm", "Read the full text"))
        self.lineEdit.setPlaceholderText(_translate("manageForm", "Enter timestamp here"))
        self.findButton.setText(_translate("manageForm", "Find"))
        self.lineEdit_2.setPlaceholderText(_translate("manageForm", "Or enter formatted time here"))
        self.findButton_2.setText(_translate("manageForm", "Find"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("manageForm", "Select by timestamp"))
        self.label_3.setText(_translate("manageForm", "year        month        day        hour       minute      second"))
        self.checkBox.setText(_translate("manageForm", "Or"))
        self.checkBox_2.setText(_translate("manageForm", "And"))
        self.pushButton_2.setText(_translate("manageForm", "Find"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("manageForm", "Select by time tuple"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("manageForm", "Select by time"))
        self.pushButton_3.setText(_translate("manageForm", "Find"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("manageForm", "Select by class"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("manageForm", "Selective reading"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("manageForm", "Read"))
        self.pushButton_4.setText(_translate("manageForm", "Clear"))
        self.cleartip.setText(_translate("manageForm", " "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("manageForm", "Clear"))
        self.pushButton_5.setText(_translate("manageForm", "Choose \na path"))
        self.outputtip.setText(_translate("manageForm", "Please choose a path!"))
        self.pushButton_6.setText(_translate("manageForm", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("manageForm", "Export"))
if not os.path.exists('./config'):
    os.mkdir('./config')
def clearly():
    try:
        os.remove('./config/config.json')
        os.remove('./config/README.txt')
        manageWindow.close()
        mainWindow.close()
        os.rmdir('./config/')
    except:
        pass
    try:
        with open(jilu_filePath,'r') as f:
            a=f.read()
        with open('./backup.bak','w') as f:
            f.write(a)
        os.remove(jilu_filePath)
        os.rmdir('./config/')
        manageWindow.close()
        mainWindow.close()
    except:
        pass
def findbytime():
    out=''
    try:
        with open(jilu_filePath,'r') as think_f:
            think_dic=json.load(think_f)
        for l in think_dic['result']:
            time_yuanzu=time.localtime(l['time'])[:6]
            if manageUi.checkBox.isChecked():
                if manageUi.yspinBox.value()==time_yuanzu[0] or manageUi.mspinBox_2.value()==time_yuanzu[1] or manageUi.dspinBox_3.value()==time_yuanzu[2] or manageUi.hspinBox_4.value()==time_yuanzu[3] or manageUi.mspinBox_5.value()==time_yuanzu[4] or manageUi.sspinBox_6.value()==time_yuanzu[5]:
                    out=out+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(l['time']))+'\n'+encodepw(l['wen'],pw)+'\n\n'
            else:
                if manageUi.yspinBox.value()==time_yuanzu[0] and manageUi.mspinBox_2.value()==time_yuanzu[1] and manageUi.dspinBox_3.value()==time_yuanzu[2] and manageUi.hspinBox_4.value()==time_yuanzu[3] and manageUi.mspinBox_5.value()==time_yuanzu[4] and manageUi.sspinBox_6.value()==time_yuanzu[5]:
                    out=out+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(l['time']))+'\n'+encodepw(l['wen'],pw)+'\n\n'
        manageUi.timefinder_2.setText(out)
    except:
        pass
def readohhhh():
    out=''
    try:
        with open(jilu_filePath,'r') as think_f:
            think_dic=json.load(think_f)
        for dic_diary in think_dic['result']:
            if dic_diary['time']==int(manageUi.lineEdit.text()):
                out=out+encodepw(dic_diary['wen'],pw)+'\n'
                break
        else:
            out='未找到相应的记录'
            if Language_now=='English':
                out='No corresponding record found'
        manageUi.timefinder.setText(out)
    except:
        manageUi.timefinder.setText('出现错误！请检查输入的字符！')
        if Language_now=='English':
            manageUi.timefinder.setText('An error occurred! Please check the entered characters!')
def readohhhhh():
    try:
        out=''
        with open(jilu_filePath,'r') as think_f:
            think_dic=json.load(think_f)
        temp=time.mktime(time.strptime(manageUi.lineEdit_2.text(),"%Y-%m-%d %H:%M:%S"))
        for dic_diary in think_dic['result']:
            if dic_diary['time']==temp:
                out=out+encodepw(dic_diary['wen'],pw)+'\n'
                break
        if out=='':
            out='未找到相应的记录'
            if Language_now=='English':
                out='No corresponding record found'
        manageUi.timefinder.setText(out)
    except:
        manageUi.timefinder.setText('出现错误！请检查输入的字符是否按"年-月-日 时:分:秒"格式！')
        if Language_now=='English':
            manageUi.timefinder.setText('An error occurred! Please check whether the entered characters are in the format of "year-month-day hour:minute:second"!')
def readohhh():
    try:
        out=''
        with open(jilu_filePath,'r') as think_f:
            think_dic=json.load(think_f)
        for l in think_dic['result']:
            out=out+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(l['time']))+'\n'
            out=out+encodepw(l['wen'],pw)+'\n\n'
        manageUi.allfinder.setText(out)
    except:
        pass
def findbyclass():
    try:
        out=''
        with open(jilu_filePath,'r') as think_f:
            think_dic=json.load(think_f)
        for dic_diary in think_dic['result']:
            if dic_diary['class']==manageUi.comboBox.currentText():
                out=out+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(dic_diary['time']))+'\n'+encodepw(dic_diary['wen'],pw)+'\n\n'
        if out=='':
            out='未找到相应的记录'
            if Language_now=='English':
                out='No corresponding record found'
        manageUi.classfinder.setText(out)
    except:
        manageUi.classfinder.setText('出现错误！')
        if Language_now=='English':
            manageUi.classfinder.setText('An error occurred!')
def manage():
    try:
        inpwUi.pushButton.clicked.disconnect(checkpw_password)
    except:
        pass
    inpwUi.pushButton.clicked.connect(checkpw_password_2)
    inpwWindow.show()
def fuyuan():
    inpwUi.label.setText('请输入密码：')
    if Language_now=='English':
        inpwUi.label.setText('Please enter the password:')
def setpassword():
    try:
        inpwUi.pushButton.clicked.disconnect(checkpw_password_2)
    except:
        pass
    inpwUi.pushButton.clicked.connect(checkpw_password)
    inpwWindow.show()
def setpw():
    inpwWindow.show()
    inpwUi.pushButton.clicked.connect(checkpw_pw)
    setpwUi.retranslateUi_pw(setpwWindow)
def checkpw_pw():
    global password
    l_thi=[]
    try:
        if inpwUi.lineEdit.text()==password:
            inpwUi.lineEdit.clear()
            jieguo=bool(setpwWindow.exec())
            if jieguo:
                pwkey=pw
                print(setpwUi.lineEdit_2.text(),type(setpwUi.lineEdit_2.text()))
                conf_dic['pwkey']=decodepw(str(int(setpwUi.lineEdit_2.text())+1642145400),200)
                with open('./config/config.json','w',encoding='utf-8') as con_f:
                    json.dump(conf_dic,con_f,indent=4)
                with open(jilu_filePath,'r',encoding='utf-8') as con_f:
                    d1=json.load(con_f)
                l_th=d1['result']
                for s2 in l_th:
                    l_thi.append({'time':s2['time'],'wen':decodepw(encodepw(s2['wen'],pwkey),int(setpwUi.lineEdit_2.text())),'class':s2['class']})
                d1['result']=l_thi
                with open(jilu_filePath,'w',encoding='utf-8') as con_f:
                    json.dump(d1,con_f,indent=4)
                setpwUi.lineEdit_2.clear()
                setpwUi.lineEdit_3.clear()
        else:
            inpwUi.label.setText('密码错误！')
            if Language_now=='English':
                inpwUi.label.setText('Wrong password!')
    except AttributeError:
        inpwUi.label.setText('请确保密钥是整数！')
        if Language_now=='English':
            inpwUi.label.setText('Make sure the key is an integer!')
def checkpw_password_2():
    global password
    if inpwUi.lineEdit.text()==password:
        manageWindow.show()
        manageUi.comboBox.clear()
        manageUi.comboBox.addItems(classList)
        inpwWindow.close()
        inpwUi.lineEdit.clear()
    else:
        inpwUi.label.setText('密码错误！')
        if Language_now=='English':
            inpwUi.label.setText('Wrong password!')
def checkpw_password():
    global password
    if inpwUi.lineEdit.text()==password:
        inpwWindow.close()
        inpwUi.lineEdit.clear()
        jieguo=bool(setpwWindow.exec())
        if jieguo:
            conf_dic['password']=decodepw(setpwUi.lineEdit_2.text(),pw)
            with open('./config/config.json','w',encoding='utf-8') as con_f:
                json.dump(conf_dic,con_f,indent=4)
    else:
        inpwUi.label.setText('密码错误！')
        if Language_now=='English':
            inpwUi.label.setText('Wrong password!')
def choosesaveFile():
    global conf_dic,jilu_filePath
    if Language_now!='English':
        jilu_filePath=QtWidgets.QFileDialog.getSaveFileName(None,"请选择存储路径",jilu_filePath,'json Flies(*.json)')[0]
    elif Language_now=='English':
        jilu_filePath=QtWidgets.QFileDialog.getSaveFileName(None,"Please select a storage path",jilu_filePath,'json Flies(*.json)')[0]
    conf_dic['filePath']=jilu_filePath
    with open('./config/config.json','w',encoding='utf-8') as con_f:
        json.dump(conf_dic,con_f,indent=4)
        settingUi.saveFiletipjson.setText('更改成功！')
        if Language_now=='English':
            settingUi.saveFiletipjson.setText('Change succeeded!')
def choosesaveFile_ma():
    global temp_filePath
    if Language_now!='English':
        temp_filePath=QtWidgets.QFileDialog.getSaveFileName(None,"请选择存储路径",'./','Text Flies(*.txt)')[0]
    elif Language_now=='English':
        temp_filePath=QtWidgets.QFileDialog.getSaveFileName(None,"Please select a storage path",'./','Text Flies(*.txt)')[0]
    manageUi.outputtip.clear()
def inputclass():
    adding_class=settingUi.lineEdit.text()
    if adding_class=='' or adding_class==' ':
        settingUi.classtip.setText('您输入的类为空!')
        if Language_now=='English':
            settingUi.classtip.setText('The class you entered<br></br> is empty!')
    else:
        settingUi.classtip.setText('')
def daochu():
    try:
        out=''
        with open(jilu_filePath,'r') as think_f:
            think_dic=json.load(think_f)
        for l in think_dic['result']:
            out=out+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(l['time']))+'\n'
            out=out+encodepw(l['wen'],pw)+'\n\n'
        with open(temp_filePath,'w',encoding='utf-8') as f:
            f.write(out)
        manageUi.outputtip.setText('导出成功！')
        if Language_now=='English':
            manageUi.outputtip.setText('Export successful!')
    except:
        pass
def addclass():
    adding_class=settingUi.lineEdit.text()
    if adding_class in classList:
        settingUi.classtip.setText('**请不要重复录入相同类!**')
        if Language_now=='English':
            settingUi.classtip.setText('**Please do not enter the<br></br> same class repeatedly!**')
    else:
        classList.append(adding_class)
        settingUi.listWidget.addItem(adding_class)
        settingUi.classtip.setText('**添加成功!**')
        if Language_now=='English':
            settingUi.classtip.setText('**Added successfully!**')
def save():
    conf_dic['class']=classList
    with open('./config/config.json','w',encoding='utf-8') as con_f:
        json.dump(conf_dic,con_f,indent=4)
    ui.comboBox.clear()
    ui.comboBox.addItems(classList)
    mainWindow.show()
    settingWindow.close()
    settingUi.lineEdit.clear()
def delclass():
    xuan=settingUi.listWidget.currentIndex().row()
    if xuan < 0:
        pass
    else:
        del classList[xuan]
        settingUi.listWidget.takeItem(xuan)
        settingUi.classtip.setText('**删除成功!**')
        if Language_now=='English':
            settingUi.classtip.setText('**Successfully deleted!**')
def setting():
    settingUi.listWidget.clear()
    settingUi.listWidget.addItems(classList)
    settingWindow.show()
    mainWindow.close()
def savethink():
    global conf_dic
    thinking=decodepw(ui.plainTextEdit.toPlainText(),pw)
    t1=int(time.time()//1)
    try:
        list = conf_dic['result']
        list.append({'time': t1, 'wen': thinking,"class":ui.comboBox.currentText()})
        conf_dic['result']=list
    except:
        conf_dic={'result':[{'time':t1,'wen':thinking,"class":ui.comboBox.currentText()}]}
    with open(jilu_filePath,'w') as fp:
        json.dump(conf_dic,fp,indent=4)
        ui.plainTextEdit.clear()
def saveconfig():
        global pw_code
        password=str(fristUi.lineEdit.text())
        s1=decodepw(password,pw)
        if 'Error' in s1:
            pw_code=False
        else:
            if fristUi.checkBox_2.isChecked():
                config_dic={'Language':'English','password':s1,'class':["Default","Reading","Feeling"],'pwkey':decodepw(str(pw+1642145400),200),'filePath':'./config/thinking.json'}
            else:
                config_dic={'Language':'Chinese','password':s1,'class':["Default","Reading","Feeling"],'pwkey':decodepw(str(pw+1642145400),200),'filePath':'./config/thinking.json'}
            with open('./config/config.json','w',encoding='utf-8') as con_f:
                json.dump(config_dic,con_f,indent=4)
            with open('./config/README.txt','w',encoding='utf-8') as con_f:
                con_f.write('请不要修改或删除此目录和此目录下的文件!\nPlease do not modify or delete this directory and the files in this directory!')
            pw_code=True
app,pw,pw_code=QtWidgets.QApplication([]),13,0
mainWindow=QtWidgets.QMainWindow()
ui=Ui_mainWindow()
ui.setupUi(mainWindow)
fristWindow=QtWidgets.QWizard()
fristUi=Ui_fristSet()
fristUi.setupUi(fristWindow)
aboutWindow=QtWidgets.QWidget()
aboutUi=Ui_aboutForm()
aboutUi.setupUi(aboutWindow)
settingWindow=QtWidgets.QWidget()
settingUi=Ui_settingsForm()
settingUi.setupUi(settingWindow)
setpwWindow=QtWidgets.QDialog()
setpwUi=Ui_setpasswordDialog()
setpwUi.setupUi(setpwWindow)
manageWindow=QtWidgets.QWidget()
manageUi=Ui_manageForm()
manageUi.setupUi(manageWindow)
inpwWindow=QtWidgets.QWidget()
inpwUi=Ui_inpwForm()
inpwUi.setupUi(inpwWindow)
if not os.path.exists('./config/config.json'):
    fristWindow.show()
    app.exec_()
    apptemp=QtWidgets.QApplication([])
    if not os.path.exists('./config/config.json'):
        if not pw_code:
            msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误/error', '加密失败，请减小密码! ! ! ! !\nEncryption failed, please reduce the password! ! ! ! !')
        else:
            msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误/error', '请设置密码! ! ! ! !\nPlease set your password! ! ! ! !')
    else:
        msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示/prompt', '程序初始化成功，请重新启动。\nProgram initialization succeeded, please restart.')
    msg_box.setWindowOpacity(0.95)
    msg_box.show()
    apptemp.exec_()
else:
    with open('./config/config.json','r') as conf_f:
        conf_dic=json.load(conf_f)
    if conf_dic['Language']=='English':
       Language_now='English'
       ui.retranslateUi_eng(mainWindow)
       aboutUi.retranslateUi_eng(aboutWindow)
       settingUi.retranslateUi_eng(settingWindow)
       setpwUi.retranslateUi_eng(setpwWindow)
       manageUi.retranslateUi_eng(manageWindow)
       inpwUi.retranslateUi_eng(inpwWindow)
    else:
        Language_now='Chinese'
    classList=conf_dic['class']
    jilu_filePath=conf_dic['filePath']
    if jilu_filePath!='./config/thinking.json':
        settingUi.saveFiletipjson.clear()
    pw=eval(encodepw(conf_dic['pwkey'],200))-1642145400
    password=encodepw(conf_dic['password'],pw)
    ui.comboBox.addItems(classList)
    mainWindow.show()
    app.exec_()