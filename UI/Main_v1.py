
import sys
from PyQt5 import QtWidgets, uic,QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import os
import json
import subprocess
import datetime
# from DATA.Databaseconnection import DatabaseConnection
from collections import Counter
import csv
import platform
import psycopg2
from psycopg2 import sql
import psutil
from PyQt5 import QtCore, QtGui ,QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


# Define database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'conveyor'
DB_USER = 'postgres'
DB_PASS = 'admin'

#ALGO_PATH="C:/INSIGHTZZ/ALGORITHM/PISTON_ARROW_V6.py"
ALGO_PATH="/home/deepak/Desktop/29/ASS/ALGORITHM/ALGORITHM_V1.py"

IMAGE_PATH="C:/INSIGHTZZ/DEFECT_DATA/"
Download_folder="C:/Users/Admin/Desktop/DOWNLOAD"


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('/home/deepak/Desktop/29/ASS/UI/Main.ui', self)
        self.dict_data=None

         # Set up the timer to update the label
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Update every second
        self.update_datetime()
        #self.part_no=None
        self.timer_3 = QTimer(self)
        self.timer_3.timeout.connect(self.showHistory)
        self.timer_3.start(1000)

        self.image_timer = QtCore.QTimer(self)
        self.image_timer.timeout.connect(self.updateImages)
        self.image_timer.start(500) 

        # self.plconnector_timer = QtCore.QTimer(self)
        # self.plconnector_timer.timeout.connect(self.check_plc_status)
        # self.plconnector_timer.start(5000) 
       
        self.NOKcount=0

        self.tableWidget.setColumnWidth(0, 138)
        self.tableWidget.setColumnWidth(1, 160)
        

        #run Algorithm backgound
        self.run_algo()

    def run_algo(self):
        try:
            # Command to run the python script
            command = ["python3", ALGO_PATH]
            # Run the command in the background
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            print(e)

    def update_datetime(self):
        current_time = QDateTime.currentDateTime()  # Get the current date and time
        formatted_time = current_time.toString('yyyy-MM-dd HH:mm:ss')  # Format it
        self.label_2.setText(formatted_time)  # Update the label text

        # Set the label's font style to bold and size to 14
        self.label_2.setStyleSheet("font-weight: bold; font-size: 14px;")

    def check_plc_status(self):
        try:
            self.plc_ip = "10.192.243.21"  # Replace with your PLC IP address
            response = subprocess.run(
                ["ping", "-c", "1", self.plc_ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if response==1:#self.ping(plc_ip):
                self.label_2.setText("PLC")
                self.label_2.setStyleSheet("background-color: rgb(255, 0, 0); font-weight: bold; font-size: 12pt;")
            else:
                self.label_2.setText("PLC")
                self.label_2.setStyleSheet("background-color: rgb(55, 255, 0); font-weight: bold; font-size: 12pt;")
        except Exception as e:
            print(e)
        

    def ping(self, host):
        try:

            """
            Returns True if host responds to a ping request
            """
            # Param "-n" (Windows) or "-c" (Unix)
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = f"ping {param} 1 {host}"
            return os.system(command) == 0
        except Exception as e:
            print(e)

    def updateImages(self):
        try:
            self.IMAGE_SAVE_PATH="/home/deepak/Desktop/29/ASS/OUTPUT/DEFECT/DEFECT_TMP.jpg"
            # Load images
            pixmap_cam1 = QPixmap(self.IMAGE_SAVE_PATH)
           
            # Display the rotated images
            self.IMAGE.setPixmap(pixmap_cam1)
            self.IMAGE.setScaledContents(True)

        except Exception as E:
            print("Error while updating image: " + str(E))
            pass
    

    def show_message(self, message):
        choice = QMessageBox.information(self, 'Message!',message)

    def fetch_today_data(self):
        data_set = []  # Initialize an empty list to store the results
        try:
            # Connect to PostgreSQL
            dbConnection = psycopg2.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                dbname=DB_NAME
            )
            cur = dbConnection.cursor()

             # Prepare the SQL query to fetch records for the current date
            query = sql.SQL("SELECT id, defect, created_time "
                            "FROM process "
                            "WHERE DATE(created_time) = CURRENT_DATE "
                            "ORDER BY id DESC;")  # Added space before "FROM"
            
            # Execute the query
            cur.execute(query)
            
            # Fetch all the results
            data_set = cur.fetchall()
        except Exception as e:
            print("fetch_today_data() Exception is: " + str(e))
            # You can also log the exception using a logger if needed
        finally:
            # Close cursor and connection
            if cur:
                cur.close()
            if dbConnection:
                dbConnection.close()
        
        return data_set
     
    
    def showHistory(self):
        try:
             
            data_set = self.fetch_today_data()
            counter = 1
            self.tableWidget.setRowCount(len(data_set))
            for row, datadict in enumerate(data_set):
                # ID = datadict[0]
                Defect = str(datadict[1])    
                # CAMERA_NAME = str(datadict[2])  
                CREATED_DATE = str(datadict[2])    
                
               
                self.tableWidget.setItem(row,0, QTableWidgetItem(Defect))
                self.tableWidget.setItem(row,1, QTableWidgetItem(CREATED_DATE))
                
               
        except Exception as e:
            print(e)
            #logger.error(f"showHistory() Exception is {e}")
    def showIMAGE(self,arg1):
        global imagewindow_object
        # print("Inside showIMAGE")
        imagewindow_object.loadImage(arg1)
    def showIMAGE_1(self,arg2):
        global imagewindow_object
        # print("Inside showIMAGE")
        imagewindow_object.loadImage_cam1(arg2)

class PhotoViewer(QtWidgets.QGraphicsView):
    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        self._zoom = 0
        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            self.photoClicked.emit(self.mapToScene(event.pos()).toPoint())
        super(PhotoViewer, self).mousePressEvent(event)   

class ImageWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ImageWindow, self).__init__()
        self.viewer = PhotoViewer(self)
        self.imagepath = "" 
        self.update_button = QtWidgets.QPushButton(self)
        self.update_button.setGeometry(QtCore.QRect(200, 0, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.update_button.setText(QtCore.QCoreApplication.translate("ImageviewWindow", ""))
        # self.update_button.clicked.connect(self.update_table)

        font = QtGui.QFont()
        font.setPointSize(15)
        self.notdefect_checkbox = QtWidgets.QCheckBox(self)
        self.notdefect_checkbox.setFont(font)
        self.notdefect_checkbox.setAutoFillBackground(True)
        self.notdefect_checkbox.setIconSize(QtCore.QSize(30, 30))
        # self.notdefect_checkbox.setObjectName("notdefect_checkbox")
        # self.notdefect_checkbox.setText(QtCore.QCoreApplication.translate("ImageviewWindow", "Not a deftect"))        
       
        self.viewer.photoClicked.connect(self.photoClicked)
        # Arrange layout
        VBlayout = QtWidgets.QVBoxLayout(self)
        VBlayout.addWidget(self.viewer)
        HBlayout = QtWidgets.QHBoxLayout()
        HBlayout.setAlignment(QtCore.Qt.AlignLeft)
        HBlayout.addWidget(self.update_button)                
        HBlayout.addWidget(self.notdefect_checkbox)        
        VBlayout.addLayout(HBlayout)
        self.imagepath = ""        

    def loadImage(self, imagelink):
        self.close()        
        self.setGeometry(100, 100, 800, 600)
        self.show()
        self.notdefect_checkbox.setChecked(False)        
        self.imagepath = imagelink        
        self.viewer.setPhoto(QtGui.QPixmap(imagelink))

    def loadImage_cam1(self, imagelink):
        self.close()        
        self.setGeometry(100, 100, 800, 600)
        self.show()
        self.notdefect_checkbox.setChecked(False)        
        self.imagepath = imagelink        
        self.viewer.setPhoto(QtGui.QPixmap(imagelink))

    def pixInfo(self):
        self.viewer.toggleDragMode()

    def photoClicked(self, pos):
        if self.viewer.dragMode()  == QtWidgets.QGraphicsView.NoDrag:
            self.editPixInfo.setText('%d, %d' % (pos.x(), pos.y()))
 
        
    def show_message(self, message):
        choice = QMessageBox.information(self, 'Message!',message)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    imagewindow_object= ImageWindow()
    window.show()
    sys.exit(app.exec())