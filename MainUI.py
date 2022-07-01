# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2Lazy2Write.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 824)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1235, 824))
        MainWindow.setMaximumSize(QtCore.QSize(1235, 824))
        MainWindow.setSizeIncrement(QtCore.QSize(1235, 824))
        MainWindow.setBaseSize(QtCore.QSize(1235, 824))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(690, 10, 531, 351))
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setObjectName("textEdit")
        self.Color_Pick = QtWidgets.QPushButton(self.centralwidget)
        self.Color_Pick.setGeometry(QtCore.QRect(1190, 440, 31, 31))
        self.Color_Pick.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Color_Pick.setStyleSheet("background-color:#000000")
        self.Color_Pick.setText("")
        self.Color_Pick.setAutoDefault(True)
        self.Color_Pick.setObjectName("Color_Pick")
        self.L_Font_Size = QtWidgets.QLabel(self.centralwidget)
        self.L_Font_Size.setGeometry(QtCore.QRect(690, 480, 131, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Font_Size.setFont(font)
        self.L_Font_Size.setLineWidth(1)
        self.L_Font_Size.setTextFormat(QtCore.Qt.PlainText)
        self.L_Font_Size.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Font_Size.setObjectName("L_Font_Size")
        self.L_Random = QtWidgets.QLabel(self.centralwidget)
        self.L_Random.setGeometry(QtCore.QRect(980, 440, 111, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Random.setFont(font)
        self.L_Random.setLineWidth(1)
        self.L_Random.setTextFormat(QtCore.Qt.PlainText)
        self.L_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Random.setObjectName("L_Random")
        self.L_Word_Horizontal = QtWidgets.QLabel(self.centralwidget)
        self.L_Word_Horizontal.setGeometry(QtCore.QRect(690, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Word_Horizontal.setFont(font)
        self.L_Word_Horizontal.setLineWidth(1)
        self.L_Word_Horizontal.setTextFormat(QtCore.Qt.PlainText)
        self.L_Word_Horizontal.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Word_Horizontal.setObjectName("L_Word_Horizontal")
        self.L_Word_Vertical = QtWidgets.QLabel(self.centralwidget)
        self.L_Word_Vertical.setGeometry(QtCore.QRect(690, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Word_Vertical.setFont(font)
        self.L_Word_Vertical.setLineWidth(1)
        self.L_Word_Vertical.setTextFormat(QtCore.Qt.PlainText)
        self.L_Word_Vertical.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Word_Vertical.setObjectName("L_Word_Vertical")
        self.L_Base = QtWidgets.QLabel(self.centralwidget)
        self.L_Base.setGeometry(QtCore.QRect(840, 440, 111, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Base.setFont(font)
        self.L_Base.setLineWidth(1)
        self.L_Base.setTextFormat(QtCore.Qt.PlainText)
        self.L_Base.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Base.setObjectName("L_Base")
        self.L_Color = QtWidgets.QLabel(self.centralwidget)
        self.L_Color.setGeometry(QtCore.QRect(1130, 440, 51, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Color.setFont(font)
        self.L_Color.setLineWidth(1)
        self.L_Color.setTextFormat(QtCore.Qt.PlainText)
        self.L_Color.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Color.setObjectName("L_Color")
        self.L_Stroke_Rotation = QtWidgets.QLabel(self.centralwidget)
        self.L_Stroke_Rotation.setGeometry(QtCore.QRect(690, 630, 131, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Stroke_Rotation.setFont(font)
        self.L_Stroke_Rotation.setLineWidth(1)
        self.L_Stroke_Rotation.setTextFormat(QtCore.Qt.PlainText)
        self.L_Stroke_Rotation.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Stroke_Rotation.setObjectName("L_Stroke_Rotation")
        self.L_Stroke_Horizontal = QtWidgets.QLabel(self.centralwidget)
        self.L_Stroke_Horizontal.setGeometry(QtCore.QRect(690, 680, 131, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Stroke_Horizontal.setFont(font)
        self.L_Stroke_Horizontal.setLineWidth(1)
        self.L_Stroke_Horizontal.setTextFormat(QtCore.Qt.PlainText)
        self.L_Stroke_Horizontal.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Stroke_Horizontal.setObjectName("L_Stroke_Horizontal")
        self.L_Stroke_Vertical = QtWidgets.QLabel(self.centralwidget)
        self.L_Stroke_Vertical.setGeometry(QtCore.QRect(690, 730, 131, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Stroke_Vertical.setFont(font)
        self.L_Stroke_Vertical.setLineWidth(1)
        self.L_Stroke_Vertical.setTextFormat(QtCore.Qt.PlainText)
        self.L_Stroke_Vertical.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Stroke_Vertical.setObjectName("L_Stroke_Vertical")
        self.Preview = QtWidgets.QPushButton(self.centralwidget)
        self.Preview.setGeometry(QtCore.QRect(1130, 500, 91, 121))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Preview.setFont(font)
        self.Preview.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Preview.setObjectName("Preview")
        self.Output = QtWidgets.QPushButton(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(1130, 640, 91, 121))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Output.setFont(font)
        self.Output.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Output.setObjectName("Output")
        self.Previwe_Box = QtWidgets.QLabel(self.centralwidget)
        self.Previwe_Box.setGeometry(QtCore.QRect(130, 90, 420, 594))
        self.Previwe_Box.setFrameShape(QtWidgets.QFrame.Box)
        self.Previwe_Box.setText("")
        self.Previwe_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.Previwe_Box.setObjectName("Previwe_Box")
        self.Left_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Left_Slider.setGeometry(QtCore.QRect(130, 50, 420, 22))
        self.Left_Slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Left_Slider.setMaximum(2545)
        self.Left_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Left_Slider.setObjectName("Left_Slider")
        self.Right_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Right_Slider.setGeometry(QtCore.QRect(130, 702, 420, 22))
        self.Right_Slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Right_Slider.setMaximum(2545)
        self.Right_Slider.setProperty("value", 2545)
        self.Right_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Right_Slider.setObjectName("Right_Slider")
        self.Top_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Top_Slider.setGeometry(QtCore.QRect(100, 90, 22, 594))
        self.Top_Slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Top_Slider.setMaximum(3765)
        self.Top_Slider.setProperty("value", 3765)
        self.Top_Slider.setOrientation(QtCore.Qt.Vertical)
        self.Top_Slider.setObjectName("Top_Slider")
        self.Bottom_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Bottom_Slider.setGeometry(QtCore.QRect(560, 90, 22, 594))
        self.Bottom_Slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Bottom_Slider.setMaximum(3765)
        self.Bottom_Slider.setOrientation(QtCore.Qt.Vertical)
        self.Bottom_Slider.setObjectName("Bottom_Slider")
        self.L_Right_Margin = QtWidgets.QLabel(self.centralwidget)
        self.L_Right_Margin.setGeometry(QtCore.QRect(260, 730, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Right_Margin.setFont(font)
        self.L_Right_Margin.setLineWidth(1)
        self.L_Right_Margin.setTextFormat(QtCore.Qt.PlainText)
        self.L_Right_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Right_Margin.setObjectName("L_Right_Margin")
        self.L_Left_Margin = QtWidgets.QLabel(self.centralwidget)
        self.L_Left_Margin.setGeometry(QtCore.QRect(260, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Left_Margin.setFont(font)
        self.L_Left_Margin.setLineWidth(1)
        self.L_Left_Margin.setTextFormat(QtCore.Qt.PlainText)
        self.L_Left_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Left_Margin.setObjectName("L_Left_Margin")
        self.L_Bottom_Margin = QtWidgets.QLabel(self.centralwidget)
        self.L_Bottom_Margin.setGeometry(QtCore.QRect(590, 340, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Bottom_Margin.setFont(font)
        self.L_Bottom_Margin.setLineWidth(1)
        self.L_Bottom_Margin.setTextFormat(QtCore.Qt.PlainText)
        self.L_Bottom_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Bottom_Margin.setObjectName("L_Bottom_Margin")
        self.L_Top_Margin = QtWidgets.QLabel(self.centralwidget)
        self.L_Top_Margin.setGeometry(QtCore.QRect(10, 340, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.L_Top_Margin.setFont(font)
        self.L_Top_Margin.setLineWidth(1)
        self.L_Top_Margin.setTextFormat(QtCore.Qt.PlainText)
        self.L_Top_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Top_Margin.setObjectName("L_Top_Margin")
        self.Font_Size_Base = QtWidgets.QSpinBox(self.centralwidget)
        self.Font_Size_Base.setGeometry(QtCore.QRect(860, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Font_Size_Base.setFont(font)
        self.Font_Size_Base.setAlignment(QtCore.Qt.AlignCenter)
        self.Font_Size_Base.setMinimum(1)
        self.Font_Size_Base.setMaximum(999)
        self.Font_Size_Base.setProperty("value", 80)
        self.Font_Size_Base.setObjectName("Font_Size_Base")
        self.Font_Size_Random = QtWidgets.QSpinBox(self.centralwidget)
        self.Font_Size_Random.setGeometry(QtCore.QRect(990, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Font_Size_Random.setFont(font)
        self.Font_Size_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.Font_Size_Random.setMinimum(0)
        self.Font_Size_Random.setMaximum(40)
        self.Font_Size_Random.setObjectName("Font_Size_Random")
        self.Word_Horizontal_Random = QtWidgets.QSpinBox(self.centralwidget)
        self.Word_Horizontal_Random.setGeometry(QtCore.QRect(990, 530, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Word_Horizontal_Random.setFont(font)
        self.Word_Horizontal_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.Word_Horizontal_Random.setMaximum(40)
        self.Word_Horizontal_Random.setObjectName("Word_Horizontal_Random")
        self.Word_Horizontal_Base = QtWidgets.QSpinBox(self.centralwidget)
        self.Word_Horizontal_Base.setGeometry(QtCore.QRect(860, 530, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Word_Horizontal_Base.setFont(font)
        self.Word_Horizontal_Base.setAlignment(QtCore.Qt.AlignCenter)
        self.Word_Horizontal_Base.setMinimum(-39)
        self.Word_Horizontal_Base.setMaximum(800)
        self.Word_Horizontal_Base.setObjectName("Word_Horizontal_Base")
        self.Word_Vertical_Base = QtWidgets.QSpinBox(self.centralwidget)
        self.Word_Vertical_Base.setGeometry(QtCore.QRect(860, 580, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Word_Vertical_Base.setFont(font)
        self.Word_Vertical_Base.setAlignment(QtCore.Qt.AlignCenter)
        self.Word_Vertical_Base.setMinimum(0)
        self.Word_Vertical_Base.setMaximum(800)
        self.Word_Vertical_Base.setObjectName("Word_Vertical_Base")
        self.Word_Vertical_Random = QtWidgets.QSpinBox(self.centralwidget)
        self.Word_Vertical_Random.setGeometry(QtCore.QRect(990, 580, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Word_Vertical_Random.setFont(font)
        self.Word_Vertical_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.Word_Vertical_Random.setMaximum(40)
        self.Word_Vertical_Random.setObjectName("Word_Vertical_Random")
        self.Stroke_Vertical_Random = QtWidgets.QSpinBox(self.centralwidget)
        self.Stroke_Vertical_Random.setGeometry(QtCore.QRect(990, 730, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Stroke_Vertical_Random.setFont(font)
        self.Stroke_Vertical_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.Stroke_Vertical_Random.setMaximum(16)
        self.Stroke_Vertical_Random.setObjectName("Stroke_Vertical_Random")
        self.Stroke_Horizontal_Random = QtWidgets.QSpinBox(self.centralwidget)
        self.Stroke_Horizontal_Random.setGeometry(QtCore.QRect(990, 680, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Stroke_Horizontal_Random.setFont(font)
        self.Stroke_Horizontal_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.Stroke_Horizontal_Random.setMaximum(16)
        self.Stroke_Horizontal_Random.setObjectName("Stroke_Horizontal_Random")
        self.Stroke_Rotation_Random = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Stroke_Rotation_Random.setGeometry(QtCore.QRect(990, 630, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Stroke_Rotation_Random.setFont(font)
        self.Stroke_Rotation_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.Stroke_Rotation_Random.setDecimals(2)
        self.Stroke_Rotation_Random.setMaximum(0.5)
        self.Stroke_Rotation_Random.setSingleStep(0.01)
        self.Stroke_Rotation_Random.setObjectName("Stroke_Rotation_Random")
        self.Font_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.Font_Text.setGeometry(QtCore.QRect(690, 370, 531, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Font_Text.setFont(font)
        self.Font_Text.setText("")
        self.Font_Text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Font_Text.setObjectName("Font_Text")
        self.Background_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.Background_Text.setGeometry(QtCore.QRect(690, 405, 531, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Background_Text.setFont(font)
        self.Background_Text.setText("")
        self.Background_Text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Background_Text.setObjectName("Background_Text")
        self.Bottom_Margin = QtWidgets.QSpinBox(self.centralwidget)
        self.Bottom_Margin.setGeometry(QtCore.QRect(585, 375, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Bottom_Margin.setFont(font)
        self.Bottom_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.Bottom_Margin.setMinimum(0)
        self.Bottom_Margin.setMaximum(3765)
        self.Bottom_Margin.setObjectName("Bottom_Margin")
        self.Top_Margin = QtWidgets.QSpinBox(self.centralwidget)
        self.Top_Margin.setGeometry(QtCore.QRect(5, 375, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Top_Margin.setFont(font)
        self.Top_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.Top_Margin.setMinimum(0)
        self.Top_Margin.setMaximum(3765)
        self.Top_Margin.setObjectName("Top_Margin")
        self.Left_Margin = QtWidgets.QSpinBox(self.centralwidget)
        self.Left_Margin.setGeometry(QtCore.QRect(340, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Left_Margin.setFont(font)
        self.Left_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.Left_Margin.setMinimum(0)
        self.Left_Margin.setMaximum(2545)
        self.Left_Margin.setObjectName("Left_Margin")
        self.Right_Margin = QtWidgets.QSpinBox(self.centralwidget)
        self.Right_Margin.setGeometry(QtCore.QRect(340, 730, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Right_Margin.setFont(font)
        self.Right_Margin.setAlignment(QtCore.Qt.AlignCenter)
        self.Right_Margin.setMinimum(0)
        self.Right_Margin.setMaximum(2545)
        self.Right_Margin.setObjectName("Right_Margin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1235, 29))
        self.menuBar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.menuBar.setAccessibleName("")
        self.menuBar.setObjectName("menuBar")
        self.Option = QtWidgets.QMenu(self.menuBar)
        self.Option.setObjectName("Option")
        self.Others = QtWidgets.QMenu(self.menuBar)
        self.Others.setObjectName("Others")
        self.Setting = QtWidgets.QMenu(self.menuBar)
        self.Setting.setObjectName("Setting")
        MainWindow.setMenuBar(self.menuBar)
        self.Font = QtWidgets.QAction(MainWindow)
        self.Font.setObjectName("Font")
        self.Background = QtWidgets.QAction(MainWindow)
        self.Background.setObjectName("Background")
        self.Save = QtWidgets.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.Load = QtWidgets.QAction(MainWindow)
        self.Load.setObjectName("Load")
        self.About = QtWidgets.QAction(MainWindow)
        self.About.setCheckable(False)
        self.About.setObjectName("About")
        self.Option.addAction(self.Font)
        self.Option.addAction(self.Background)
        self.Others.addAction(self.About)
        self.Setting.addAction(self.Save)
        self.Setting.addAction(self.Load)
        self.menuBar.addAction(self.Option.menuAction())
        self.menuBar.addAction(self.Setting.menuAction())
        self.menuBar.addAction(self.Others.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2Lazy2Write"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "请在此输入待处理文本"))
        self.L_Font_Size.setText(_translate("MainWindow", "字号"))
        self.L_Random.setText(_translate("MainWindow", "随机增减值"))
        self.L_Word_Horizontal.setText(_translate("MainWindow", "字水平间距"))
        self.L_Word_Vertical.setText(_translate("MainWindow", "字垂直间距"))
        self.L_Base.setText(_translate("MainWindow", "基础"))
        self.L_Color.setText(_translate("MainWindow", "颜色"))
        self.L_Stroke_Rotation.setText(_translate("MainWindow", "笔画旋转"))
        self.L_Stroke_Horizontal.setText(_translate("MainWindow", "笔画水平偏移"))
        self.L_Stroke_Vertical.setText(_translate("MainWindow", "笔画垂直偏移"))
        self.Preview.setText(_translate("MainWindow", "预览"))
        self.Output.setText(_translate("MainWindow", "导出"))
        self.L_Right_Margin.setText(_translate("MainWindow", "右边距"))
        self.L_Left_Margin.setText(_translate("MainWindow", "左边距"))
        self.L_Bottom_Margin.setText(_translate("MainWindow", "下边距"))
        self.L_Top_Margin.setText(_translate("MainWindow", "上边距"))
        self.Font_Text.setPlaceholderText(_translate("MainWindow", "请在左上角(选项 - 字体)中选择并设置字体"))
        self.Background_Text.setPlaceholderText(_translate("MainWindow", "请在左上角(选项 - 底纸)中选择并设置底纸"))
        self.Option.setTitle(_translate("MainWindow", "选项"))
        self.Others.setTitle(_translate("MainWindow", "其他"))
        self.Setting.setTitle(_translate("MainWindow", "配置"))
        self.Font.setText(_translate("MainWindow", "字体"))
        self.Background.setText(_translate("MainWindow", "底纸"))
        self.Save.setText(_translate("MainWindow", "保存"))
        self.Save.setToolTip(_translate("MainWindow", "保存"))
        self.Save.setStatusTip(_translate("MainWindow", "保存除字体底纸外的参数配置"))
        self.Load.setText(_translate("MainWindow", "载入"))
        self.Load.setToolTip(_translate("MainWindow", "载入"))
        self.Load.setStatusTip(_translate("MainWindow", "载入除字体底纸外的参数配置"))
        self.About.setText(_translate("MainWindow", "关于"))
