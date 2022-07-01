import sys
from MainUI import Ui_MainWindow, QtGui
from AboutUI import Ui_AboutForm
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog
from PyQt5.QtCore import Qt
from PIL import Image, ImageFont, ImageQt
from handright import Template, handwrite

PreColor = '#000000' # 全局变量颜色

def getfile(parent,caption,directory,filetype):
    global FontFile, BackgroundFile
    q = QFileDialog.getOpenFileName(parent,caption,directory,filetype)
    return q[0]

def savefile(parent,caption,directory,filetype):
    q = QFileDialog.getSaveFileName(parent,caption,directory,filetype)
    return q[0]

class mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Font.triggered.connect(lambda:self.Font_Text.setText(getfile(self,'打开','','TrueType 字体文件 (*.ttf)')))
        self.Background.triggered.connect(lambda:self.Background_Text.setText(getfile(self,'打开','','Image 图片文件 (*.jpg *.png *.jpeg)')))
        self.Font_Size_Base.valueChanged.connect(lambda:self.MaxValueFix())
        self.Left_Slider.valueChanged.connect(lambda:self.spliderchange('L'))
        self.Left_Margin.valueChanged.connect(lambda:self.spinboxchange('L'))
        self.Right_Slider.valueChanged.connect(lambda:self.spliderchange('R'))
        self.Right_Margin.valueChanged.connect(lambda:self.spinboxchange('R'))
        self.Top_Slider.valueChanged.connect(lambda:self.spliderchange('T'))
        self.Top_Margin.valueChanged.connect(lambda:self.spinboxchange('T'))
        self.Bottom_Slider.valueChanged.connect(lambda:self.spliderchange('B'))
        self.Bottom_Margin.valueChanged.connect(lambda:self.spinboxchange('B'))
        self.Color_Pick.clicked.connect(self.ColorPick)
        self.Preview.clicked.connect(self.PreviewPaper)
        self.Output.clicked.connect(self.OutputPaper)
        self.Save.triggered.connect(self.SaveSetting)
        self.Load.triggered.connect(self.LoadSetting)
        self.About.triggered.connect(self.OpenAboutWindow)

    def MaxValueFix(self):
        Font_Base = int(self.Font_Size_Base.value())
        self.Font_Size_Random.setMaximum(Font_Base//2)
        self.Word_Horizontal_Base.setRange((-1)*Font_Base//2+1, Font_Base*10)
        self.Word_Horizontal_Random.setMaximum(Font_Base//2)
        self.Word_Vertical_Base.setMaximum(Font_Base*10)
        self.Word_Vertical_Random.setMaximum(Font_Base//2)
        self.Stroke_Horizontal_Random.setMaximum(Font_Base//5)
        self.Stroke_Vertical_Random.setMaximum(Font_Base//5)

    def spliderchange(self, location):
        if location == 'L':
            self.Left_Margin.setValue(self.Left_Slider.value())
        elif location == 'R':
            self.Right_Margin.setValue(2545 - self.Right_Slider.value())
        elif location == 'T':
            self.Top_Margin.setValue(3765 - self.Top_Slider.value())
        elif location == 'B':
            self.Bottom_Margin.setValue(self.Bottom_Slider.value())

    def spinboxchange(self, location):
        if location == 'L':
            self.Left_Slider.setValue(self.Left_Margin.value())
        elif location == 'R':
            self.Right_Slider.setValue(2545 - self.Right_Margin.value())
        elif location == 'T':
            self.Top_Slider.setValue(3765 - self.Top_Margin.value())
        elif location == 'B':
            self.Bottom_Slider.setValue(self.Bottom_Margin.value())    
    
    def ColorPick(self):
        global PreColor
        color = QColorDialog.getColor(
            initial= QtGui.QColor(PreColor), # 初始颜色
            parent = None, # 父窗口
            title = '文字颜色设置') # 颜色框标题
        PreColor = str(color.name())
        if color.isValid(): # 用户的新颜色
            self.Color_Pick.setStyleSheet('background-color:{0}'.format(color.name()))

    def SaveSetting(self):
        file_path = savefile(self,'保存','','(*.lw)')
        if file_path != "":
            file_text = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s"% (
                self.Left_Margin.text(),
                self.Right_Margin.text(),
                self.Top_Margin.text(),
                self.Bottom_Margin.text(),
                self.Color_Pick.styleSheet()[17:24],
                self.Font_Size_Base.text(),
                self.Font_Size_Random.text(),
                self.Word_Horizontal_Base.text(),
                self.Word_Horizontal_Random.text(),
                self.Word_Vertical_Base.text(),
                self.Word_Vertical_Random.text(),
                self.Stroke_Rotation_Random.text(),
                self.Stroke_Horizontal_Random.text(),
                self.Stroke_Vertical_Random.text())
            with open(file=file_path, mode='w', encoding='utf-8') as file:
                file.write(file_text)

    def LoadSetting(self):
        global PreColor
        file_path = getfile(self,'载入','','(*.lw)')
        if file_path != "":
            Data = []
            if file_path is not None:
                with open(file=file_path, mode='r+', encoding='utf-8') as f:
                    for line in f.readlines():
                        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                        Data.append(line)
            self.Left_Margin.setValue(int(Data[0]))
            self.Right_Margin.setValue(int(Data[1]))
            self.Top_Margin.setValue(int(Data[2]))
            self.Bottom_Margin.setValue(int(Data[3]))
            PreColor = str(Data[4])
            self.Color_Pick.setStyleSheet('background-color:{0}'.format(str(Data[4])))
            self.Font_Size_Base.setValue(int(Data[5]))
            self.Font_Size_Random.setValue(int(Data[6]))
            self.Word_Horizontal_Base.setValue(int(Data[7]))
            self.Word_Horizontal_Random.setValue(int(Data[8]))
            self.Word_Vertical_Base.setValue(int(Data[9]))
            self.Word_Vertical_Random.setValue(int(Data[10]))
            self.Stroke_Rotation_Random.setValue(float(Data[11]))
            self.Stroke_Horizontal_Random.setValue(int(Data[12]))
            self.Stroke_Vertical_Random.setValue(int(Data[13]))
            
    def PreviewPaper(self):
        text = self.textEdit.toPlainText()
        FontText = self.Font_Text.text()
        BackgroundText = self.Background_Text.text()
        WordHorizontalBase = self.Word_Horizontal_Base.text()
        WordHorizontalRandom = self.Word_Horizontal_Random.text()
        WordVerticalBase = self.Word_Vertical_Base.text()
        WordVerticalRandom = self.Word_Vertical_Random.text()
        FontSizeBase = self.Font_Size_Base.text()
        FontSizeRandom = self.Font_Size_Random.text()
        StrokeVerticalRandom = self.Stroke_Vertical_Random.text()
        StrokeHorizontalRandom = self.Stroke_Horizontal_Random.text()
        StrokeRotationRandom = self.Stroke_Rotation_Random.text()
        LeftMargin = self.Left_Margin.text()
        RightMargin = self.Right_Margin.text()
        TopMargin = self.Top_Margin.text()
        BottomMargin = self.Bottom_Margin.text()
        hex = PreColor.lstrip('#')
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        if text == "" or FontText == "" or WordHorizontalBase == "" or BottomMargin == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整", QMessageBox.Yes)
        else:
            template = Template(
                background=Image.open(BackgroundText),
                font=ImageFont.truetype(FontText, size=int(FontSizeBase)),
                line_spacing=int(WordVerticalBase) + int(FontSizeBase),
                fill=rgb,  # 字体“颜色”
                left_margin=int(LeftMargin),
                top_margin=int(TopMargin),
                right_margin=int(RightMargin) - int(WordHorizontalBase) * 2,
                bottom_margin=int(BottomMargin),
                word_spacing=int(WordHorizontalBase),
                line_spacing_sigma=int(WordVerticalRandom),  # 行间距随机扰动
                font_size_sigma=int(FontSizeRandom),  # 字体大小随机扰动
                word_spacing_sigma=int(WordHorizontalRandom),  # 字间距随机扰动
                end_chars="，。—！？,.!?》）、”",  # 防止特定字符因排版算法的自动换行而出现在行首
                perturb_x_sigma=int(StrokeVerticalRandom),  # 笔画横向偏移随机扰动
                perturb_y_sigma=int(StrokeHorizontalRandom),  # 笔画纵向偏移随机扰动
                perturb_theta_sigma=float(StrokeRotationRandom),  # 笔画旋转偏移随机扰动
            )
            images = handwrite(text, template)
            for i, im in enumerate(images): # i不调用，仅用于限制输出一张
                im = im.convert("RGBA")
                image = ImageQt.toqpixmap(im)
                self.Previwe_Box.setScaledContents(True)
                self.Previwe_Box.setPixmap(image)
                break

    def OutputPaper(self):
        text = self.textEdit.toPlainText()
        FontText = self.Font_Text.text()
        BackgroundText = self.Background_Text.text()
        WordHorizontalBase = self.Word_Horizontal_Base.text()
        WordHorizontalRandom = self.Word_Horizontal_Random.text()
        WordVerticalBase = self.Word_Vertical_Base.text()
        WordVerticalRandom = self.Word_Vertical_Random.text()
        FontSizeBase = self.Font_Size_Base.text()
        FontSizeRandom = self.Font_Size_Random.text()
        StrokeVerticalRandom = self.Stroke_Vertical_Random.text()
        StrokeHorizontalRandom = self.Stroke_Horizontal_Random.text()
        StrokeRotationRandom = self.Stroke_Rotation_Random.text()
        LeftMargin = self.Left_Margin.text()
        RightMargin = self.Right_Margin.text()
        TopMargin = self.Top_Margin.text()
        BottomMargin = self.Bottom_Margin.text()
        hex = PreColor.lstrip('#')
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        if text == "" or FontText == "" or WordHorizontalBase == "" or BottomMargin == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整", QMessageBox.Yes)
        else:
            template = Template(
                background=Image.open(BackgroundText),
                font=ImageFont.truetype(FontText, size=int(FontSizeBase)),
                line_spacing=int(WordVerticalBase) + int(FontSizeBase),
                fill=rgb,  # 字体“颜色”
                left_margin=int(LeftMargin),
                top_margin=int(TopMargin),
                right_margin=int(RightMargin) - int(WordHorizontalBase) * 2,
                bottom_margin=int(BottomMargin),
                word_spacing=int(WordHorizontalBase),
                line_spacing_sigma=int(WordVerticalRandom),  # 行间距随机扰动
                font_size_sigma=int(FontSizeRandom),  # 字体大小随机扰动
                word_spacing_sigma=int(WordHorizontalRandom),  # 字间距随机扰动
                end_chars="，。—！？,.!?》）、”",  # 防止特定字符因排版算法的自动换行而出现在行首
                perturb_x_sigma=int(StrokeVerticalRandom),  # 笔画横向偏移随机扰动
                perturb_y_sigma=int(StrokeHorizontalRandom),  # 笔画纵向偏移随机扰动
                perturb_theta_sigma=float(StrokeRotationRandom),  # 笔画旋转偏移随机扰动
            )
            images = handwrite(text, template)
            for i, im in enumerate(images):
                assert isinstance(im, Image.Image)
                im.save("./{}.png".format(i))

    def OpenAboutWindow(self):
        self.UI2 = aboutwindow()
        self.UI2.show()

class aboutwindow(QMainWindow, Ui_AboutForm):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_AboutForm.__init__(self)
        self.setupUi(self)
        

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    UI = mainwindow()  # 创建自定义ui界面
    UI.show()
    app.exec_()