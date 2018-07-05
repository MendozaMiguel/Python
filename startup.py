try:
    import os
except ImportError:
  print ("Trying to Install required module: os")
  os.system('python -m pip install os')

try:
    import pandas as pd
except ImportError:
  print ("Trying to Install required module: pandas")
  os.system('python -m pip install pandas')

pd.set_option("expand_frame_repr",False)
pd.options.display.max_rows=10#limite l'affiche dans des lings
pd.options.display.max_columns=10#cols
pd.set_option('colheader_justify', 'left')#alignement de titles
pd.set_option('precision',3)#nombres apres le . ## numero 0.123
pd.set_option('max_colwidth',10)#limiter l'affichage de grands phrases par exemple dans une cellule

#############################WINDOWS#######################
#SETX PATH "%PATH%;C:\Users\YSK_9\Anaconda3\Scripts;C:\Users\YSK_9\Anaconda3"
############################VARIABLES######################

try:
    import numpy as np
except ImportError:
  print ("Trying to Install required module: numpy")
  os.system('python -m pip install numpy')  
  
try:
    import random
except ImportError:
  print ("Trying to Install required module: random")
  os.system('python -m pip install random')  
  
try:
    import time
except ImportError:
  print ("Trying to Install required module: time")
  os.system('python -m pip install time')  
  
  
try:
    import pickle
except ImportError:
  print ("Trying to Install required module: pickle")
  os.system('python -m pip install pickle')  
  

#import numpy as np
#import random
#import os
#import time
#import pickle

#try:
 # import requests
#except ImportError:
 # print "Trying to Install required module: requests\n"
  #os.system('python -m pip install requests')
  
  
my_path = "C:/Users/YSK_9/Desktop/DATA" #change le path
if not os.path.exists(my_path):
   os.makedirs(my_path)

if os.getcwd() != my_path :
    os.chdir(my_path)
print(my_path)


#df.get_dtype_counts()
####################JUPYTER######################
########install nbextension jupyter########
#pip install jupyter_contrib_nbextensions
#jupyter contrib nbextension install --user
#jupyter nbextension enable varInspector/main
####################JUPYTER######################