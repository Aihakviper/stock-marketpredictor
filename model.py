from sklearn.model_selection import train_test_split
import joblib
from sklearn.linear_model import LinearRegression
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from main import x,y


#spilitting data
x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)

# setting up model hyperparameters
modele = ensemble.GradientBoostingRegressor(
n_estimators=150,
learning_rate=0.1,
max_depth=30,
min_samples_split=4,
min_samples_leaf=6,
max_features=0.6,
loss='huber'
)
modell = LinearRegression(fit_intercept=True, n_jobs=-1, positive=False)

modelr = ensemble.RandomForestRegressor(n_estimators=100,random_state=1)
modelr1 = ensemble.RandomForestRegressor(n_estimators=150,random_state=2)
modelr2 = ensemble.RandomForestRegressor(n_estimators=200,random_state=2)
modelr3 = ensemble.RandomForestRegressor(n_estimators=50,random_state=1)
modelr4 = ensemble.RandomForestRegressor(n_estimators=100,random_state=2)

modelg = ensemble.GradientBoostingRegressor()

models = [modele,modell,modelr, modelr1, modelr2, modelr3, modelr4 modelg]

def score_test(model,xt = x_train, xte = x_test, yt = y_train, yte = y_test):
    model.fit(xt, yt)
    preds = model.predict(xte)
    return mean_absolute_error(yte, preds)

for i in range(0, len(models)):
    mae = score_test(models[i])
    print(f"Model {i+1} MAE: {mae:.4f}")

modelr4.fit(x_train, y_train)

#saving model to a file
joblib.dump(modelr4, "trained_model.joblib")
joblib.dump(x_train.columns.tolist(), "model_features.pkl")





