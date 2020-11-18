import numpy as np
import pandas as pd
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Forest_fire.csv")
data = np.array(data)

x = data[2:, 2:-1]
y = data[2:, -1]

le = LabelEncoder()        # YES = 1, NO = 0
y = le.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

sv = SVC(kernel = 'linear').fit(x_train,y_train)

pickle.dump(sv, open('model.pkl', 'wb'))
