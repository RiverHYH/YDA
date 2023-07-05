# **BackGround**
This Python package by RiverHYH aims to simplify the data analysis process.
# **Claims**
All modules are open-sourced.

# **ChangeLog**
This version is the first pre-release version which includes several changes listed below:
**- Add**
  - Add new function Environment.SetEnv(): This function will automatically
    check the availability of several useful packages used in data analysis.(numpy, pandas,sklearn,matplotlib, seaborn)
  - Add new function Environment.BreakPoint(): This function allows users to customise their breakpoints in Jupyter Notebook.
    The running process will be paused when reaching BreakPoint(). Users could either cease the running by entering True or continue running by False.
  - Add new function Process.MinMaxNormaliser(Array: list): This function normalises continuous values in the input array.
  - Add new function Process.GetTrainTime(Model,X_Train,Y_Train): This function will give the training time of an ML model and return a fitted model.
  - Add new function Visual.GetCorrHeat(df: pandas.DataFrame): This function generates product correlation coefficients of between each given feature.
  - Add new function Visual.GetROC(X_Test,Y_Test,Trained_Estimator): This functions will plot out ROC and provides AUC of a trained ML models
    
