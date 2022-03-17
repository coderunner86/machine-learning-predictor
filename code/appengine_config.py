# appengine_config.py
from google.appengine.ext import vendor

import os

#This will remove all *.pyc files and pycache directories recursively in the current directory:
os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
# Add any libraries install in the "lib" folder.
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
