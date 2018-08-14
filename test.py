import subprocess

import scipy.misc
from google.cloud import storage
from tensorflow.python.lib.io import file_io

# subprocess.check_call(['mkdir', './trainer/datasets'])
# subprocess.check_call(['gsutil', '-m', 'cp', '-r',
#                            'gs://goagent01-1146-mlengine/datasets', './trainer/datasets'])
file = file_io.FileIO('gs://goagent01-1146-mlengine/datasets/anime/trainA/1. bcg.jpg', mode='r')
img = scipy.misc.imread(file)
print(img)

