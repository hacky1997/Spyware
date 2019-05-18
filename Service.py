import pyunpack
from pyunpack import Archive
import wget 

url = "http://s000.tinyupload.com/index.php?file_id=06899067767668620274"
wget.download(url)
Archive('Adobe.zip').extractall('.')



