
# coding: utf-8

# In[1]:

import numpy as np
import glob


# In[2]:

def dwelling_id_list():
    path = '/datc/opschaler/smartmeter_data'
    file_paths = np.array(glob.glob(path + "/*.csv"))
    dwelling_ids = np.array(list((map(lambda x: x[-15:-4], file_paths))))
    return list(dwelling_ids)


# In[ ]:



