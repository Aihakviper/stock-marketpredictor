from sklearn.model_selection import train_test_split
import joblib
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from main import x,y


#spilitting data
x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)

# setting up model hyperparameters
modelr = ensemble.RandomForestRegressor(n_estimators=100,random_state=2)

modelr.fit(x_train, y_train)

#saving model to a file
joblib.dump(modelr, "trained_model.joblib")
joblib.dump(x_train.columns.tolist(), "model_features.pkl")





