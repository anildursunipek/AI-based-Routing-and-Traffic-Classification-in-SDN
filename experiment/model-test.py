import xgboost as xgb
import numpy as np

# XGBOOST model prediction example
loaded_model = xgb.XGBClassifier()
loaded_model.load_model('models/xgboost_binary_classification.json')

data = [1.75510600e+03, 1.24000000e+01, 5.12784975e+05, 9.48721503e+01,
        7.00000000e+01, 4.54106800e+00, 3.88570200e+00, 1.23810000e+04,
        1.23810000e+04, 1.02650000e+04, 6.19050000e+02, 8.93977715e+02,
        3.29700000e+03, 1.23810000e+03, 9.47748613e+02, 3.32200000e+03,
        1.14055556e+03, 1.08594027e+03, 3.32300000e+03]

data = np.array([data])
prediction = loaded_model.predict(data)

print(prediction)
print(type(prediction))