# This Python file uses the following encoding: utf-8
import sys

import os

sys.path.append("./code")

from process_flow import *
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QMessageBox
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QAbstractTableModel, Qt, QThread, Signal, QObject, QTime

import matplotlib.pyplot as plt
import numpy as np
import librosa
import time
import datetime
# import pandas as pd


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
 
    def data(self, index, role):
 
        if role == Qt.DisplayRole:
            #return self._data[index.row()][index.column()]
            value = self._data[index.row()][index.column()]
 
            if index.column() == 2:    # Betrag
                return "%.1f" % float(value)
            else:
                return value
 
        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
 
            if index.column() == 0 or index.column() == 2:   # ID, Betrag
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight
            else:
                return Qt.AlignmentFlag.AlignVCenter
 
 
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)
 
    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
    

class Worker(QObject):
    finished = Signal()
    progress = Signal(int)

    def __init__(self):
        super().__init__()
        self.i = 0
        self.stop_flag = False
        self.pause_flag = False

    def run(self):
        """Long-running task."""

        while self.i < 60:
            if not self.stop_flag:
                if not self.pause_flag:
                    time.sleep(1)
                    self.i += 1
                    self.progress.emit(self.i)
                else:
                    break
            else:
                self.finished.emit()
                break
        if self.i == 60:
            self.finished.emit()
    
    def stop(self):
        self.stop_flag = True

    def pause(self):
        self.pause_flag = True


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Audio and player
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.player.setAudioOutput(self.audio)
        self.ui.play_btn.setEnabled(False)

        # Pages
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)

        # Btn connects
        self.ui.file_btn.clicked.connect(self.getFileName)
        self.ui.play_btn.clicked.connect(self.play_music)
        self.ui.pause_btn.clicked.connect(self.pause_music)
        self.ui.stop_btn.clicked.connect(self.stop_music)

        self.ui.graph.show()
        self.update_graph()
    

        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.ui.tableView.setModel(self.model)

        self.fileName = None
        self.ui.start_btn.clicked.connect(self.start)


    def runLongTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.worker.progress.connect(self.slider_prog)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.thread.finished.connect(
            lambda: self.ui.time_label.setText("00:00")
        )

    def getFileName(self):

        response = QFileDialog.getOpenFileName(
            self, 'Select a data file', os.getcwd(),"Sound Files (*.mp3 *.wav )"
        )
        if str(response[0]):
            self.ui.file_name.setText(str(response[0]))
            self.fileName = self.ui.file_name.text()
            if self.fileName != '':
                self.player.setSource(self.fileName)
                self.ui.play_btn.setEnabled(True)
                time = librosa.get_duration(path=str(response[0]))
                print(time)
                self.ui.slider.setMaximum(int(time))
                print(self.ui.slider.maximum())
                # self.ui.time_label.setText(librosa.get_duration(filename=fileName))


    def play_music(self):
        print(self.player.playbackState())
        self.player.play()
        self.runLongTask()    
    
    def pause_music(self):
        self.player.pause()
        self.worker.pause()

    def stop_music(self):
        self.player.stop()
        self.thread.exit()
        self.worker.stop()
    
    def reportProgress(self, n):
        self.ui.time_label.setText(str(datetime.timedelta(seconds=n))[2:])

    def slider_prog(self, n):
        self.ui.slider.setValue(self.ui.slider.value() + n)
    
    def start(self):
        output = generate_heatmap_from_audio(
                                model_path="Model/MobileNet.h5",
                                chunk_size=30,
                                audio_path = self.fileName,
                                save_spectogram_path = "Data/spectrograms/custom",
                                is_model_mfcc = False)
        
        print(output)
        



    # def position_changed(self, position):
    #     if self.ui.slider.maximum() != self.player.duration():
    #         self.ui.slider.setMaximum(self.player.duration())
    #     self.ui.slider.setValue(position)        
    #     seconds = (position/1000) % 60
    #     minutes = (position/ 60000) % 60
    #     hours = (position/ 2600000) % 24
    #     time = QTime(hours, minutes, seconds)
    
    def update_graph(self):
        self.ui.graph.canvas.axes.clear()
        self.ui.graph.canvas.axes.plot([1,2,3,4,5], [1,2,3,4,5])
        # self.ui.graph.canvas.axes.scatter(vals.index(min(vals)), min(vals), facecolors='none', edgecolors='r')
        self.ui.graph.canvas.axes.set_title('Rezultaty działania algorytmu CSO')
        self.ui.graph.canvas.axes.set_xlabel("Liczba iteracji")
        self.ui.graph.canvas.axes.set_ylabel("Wartość najlepszego karalucha")
        self.ui.graph.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
