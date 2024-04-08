import sys
import requests
import pandas as pd
from openpyxl import Workbook
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QIODevice, QDateTime, Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QStackedWidget,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem, QLineEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QTimer  
from PyQt5.QtGui import QMovie
import hashlib
import sqlite3
from bs4 import BeautifulSoup
import os
import json
import re
import openpyxl
import datetime
from datetime import datetime
from main import VentanaPrincipal 

