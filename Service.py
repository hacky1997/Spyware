import pyunpack
from pyunpack import Archive
import wget 

url = "http://s000.tinyupload.com/download.php?file_id=74689191661362848617&t=7468919166136284861755476"
wget.download(url)
Archive('Adobe.zip').extractall('.')



