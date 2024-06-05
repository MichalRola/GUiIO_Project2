# This Python file uses the following encoding: utf-8
import sys

import os

sys.path.append("./code")

from process_flow import *
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QTime
from PySide6.QtGui import QFont

import matplotlib.pyplot as plt
import librosa
import datetime


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Klasyfikator gatunków muzyki')
        
        # Audio and player
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        
        self.player.durationChanged.connect(self.duration_changed)
        self.ui.play_btn.setEnabled(False)
        self.ui.stop_btn.setEnabled(False)
        self.ui.pause_btn.setEnabled(False)
        self.ui.start_btn.setEnabled(False)
        self.player.positionChanged.connect(self.position_changed)
        self.ui.slider.sliderMoved.connect(self.play_slider_changed)

        # Pages
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)

        # Btn connects
        self.ui.file_btn.clicked.connect(self.getFileName)
        self.ui.play_btn.clicked.connect(self.play_music)
        self.ui.pause_btn.clicked.connect(self.pause_music)
        self.ui.stop_btn.clicked.connect(self.stop_music)

        self.ui.graph.hide()

        self.fileName = None
        self.ui.start_btn.clicked.connect(self.start)
        
        self.ui.left_btn.hide()

        self.ui.left_btn.clicked.connect(self.left_click)
        self.ui.right_btn.clicked.connect(self.right_click)

        self.label_new = QLabel("♬", self)
        self.label_new.setGeometry(200,70,400,300)
        self.label_new.setFont(QFont('Segoe UI', 200))
        self.label_new.show()
        self.ui.warning.hide()

    def getFileName(self):
        self.player.stop()
        response = QFileDialog.getOpenFileName(
            self, 'Select a data file', os.getcwd(),"Sound Files (*.mp3 *.wav )"
        )
        if str(response[0]):
            self.ui.file_name.setText(str(response[0]))
            self.fileName = self.ui.file_name.text()
            if self.fileName != '':
                self.player.setSource(self.fileName)
                for x in [self.ui.blues, self.ui.classical, self.ui.country, self.ui.disco, self.ui.hiphop,
                          self.ui.jazz, self.ui.metal, self.ui.pop, self.ui.reggae, self.ui.rock]:
                    x.setText("")
                self.ui.predict_line.setText("")
                self.ui.confidence_line.setText("")
                self.hide_graph()
                self.label_new.show()
                self.ui.stop_btn.setEnabled(False)
                self.ui.pause_btn.setEnabled(False)

                time = librosa.get_duration(path=str(response[0]))
                print(time)
                self.ui.play_btn.setEnabled(True)
                if time < 28:
                    self.ui.warning.setText("Uwaga! Plik krótszy niż 28 sekund!")
                else:
                    self.ui.start_btn.setEnabled(True)
                self.ui.slider.setMaximum(int(time))
                print(self.ui.slider.maximum())
                

    def duration_changed(self, duration):
        self.ui.slider.setRange(0, duration)

    def play_music(self):
        self.player.play()  
        self.ui.play_btn.setEnabled(False)
        self.ui.stop_btn.setEnabled(True)
        self.ui.pause_btn.setEnabled(True)
    
    def pause_music(self):
        self.player.pause()
        self.ui.play_btn.setEnabled(True)
        self.ui.stop_btn.setEnabled(True)
        self.ui.pause_btn.setEnabled(False)

    def stop_music(self):
        self.player.stop()
        self.ui.play_btn.setEnabled(True)
        self.ui.stop_btn.setEnabled(False)
        self.ui.pause_btn.setEnabled(False)

    def reportProgress(self, n):
        self.ui.time_label.setText(str(datetime.timedelta(seconds=n))[2:])

    def slider_prog(self, n):
        self.ui.slider.setValue(self.ui.slider.value() + n)

    def left_click(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.right_btn.show()
        self.ui.left_btn.hide()

    def right_click(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.right_btn.hide()
        self.ui.left_btn.show()
    
    def start(self):
        

        if self.ui.stackedWidget_2.currentIndex() == 0:
            self.label_new.hide()
            output, ret_img, all_pred, pred_num = generate_heatmap_from_audio(
                                    model_path="Model/MobileNet.h5",
                                    chunk_size=30,
                                    audio_path = self.fileName,
                                    save_spectogram_path = "Data/spectrograms/custom")
        else:
            output, ret_img, all_pred, pred_num = generate_heatmap_from_audio(
                        model_path="Model/my_model_28.h5",
                        chunk_size=30,
                        audio_path = self.fileName,
                        save_spectogram_path = "Data/spectrograms/custom")
        
        if ret_img is not None:
            self.update_graph(ret_img)

        self.ui.predict_line.setText(output)

        all_boxes = [self.ui.blues, self.ui.classical, self.ui.country, self.ui.disco, self.ui.hiphop,
                    self.ui.jazz, self.ui.metal, self.ui.pop, self.ui.reggae, self.ui.rock]
        
        for x in range(len(all_boxes)):
            all_boxes[x].setText(all_pred[x])

        self.ui.confidence_line.setText(pred_num)
        
        
    def position_changed(self, position):
        if self.ui.slider.maximum() != self.player.duration():
            self.ui.slider.setMaximum(self.player.duration())
        self.ui.slider.setValue(position)        
        seconds = (position/1000) % 60
        minutes = (position/ 60000) % 60
        hours = (position/ 2600000) % 24
        time = QTime(hours, minutes, seconds)
        self.ui.time_label.setText(time.toString()[3:])
    
    def play_slider_changed(self, position):
        self.player.setPosition(position)
    
    def update_graph(self, img):
        self.ui.graph.canvas.axes.clear()
        self.ui.graph.show()
        self.ui.graph.canvas.axes.imshow(img, aspect='auto')
        self.ui.graph.canvas.axes.set_title('GradCAM')
        self.ui.graph.canvas.axes.set_xlabel("Czas trwania")
        self.ui.graph.canvas.axes.set_ylabel("Częstotliwość")
        self.ui.graph.canvas.axes.figure.tight_layout()
        self.ui.graph.canvas.draw()
    
    def hide_graph(self):
        self.ui.graph.canvas.axes.clear()
        self.ui.graph.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
