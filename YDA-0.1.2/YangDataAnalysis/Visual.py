def GetCorrHeat(df):

    try:
        sns.set_context({'figure.figsize':[20, 20]}) #Set Fig Size
    except:
        raise("Dependencies Unsatisfied.You can use 'SetEnv()'to set up the dependencies")
    
   
    Corr=df.corr(numeric_only=True)
    #Create a triangle masks to cover dublicated coeficients
    mask = np.zeros_like(Corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
         #Generate Heatmap ranged[1:-1] and centred 0
        sns.heatmap(Corr,cmap="RdBu_r",annot=True,linewidths=1,fmt=".1g",center=0,vmax=1,vmin=-1,mask=mask)
        
def GetROC(X_Test,Y_Test,Trained_Estimator):
    sns.set_context({'figure.figsize':[5, 5]})
    
    from sklearn.metrics import RocCurveDisplay,roc_auc_score
    #Get AUC
    if hasattr(Trained_Estimator, 'predict_proba'):
        y_pred_prob = Trained_Estimator.predict_proba(X_Test)[:,1]
    elif hasattr(Trained_Estimator, 'decision_function'):
        y_pred_prob = Trained_Estimator.decision_function(X_Test)
    else:
        raise ValueError(f"{Trained_Estimator} has no attribute 'predict_proba'or'decision_function'")
    auc = roc_auc_score(Y_Test, y_pred_prob)
    #Plot ROC Curve
    RocCurveDisplay.from_estimator(estimator=Trained_Estimator,X=X_Test,y=Y_Test,response_method="auto")
    
    plt.show()
    
    
    model_name=str(type(Trained_Estimator)).split('.')[-1].split('’')[0][:-2]#extracting the name of the models
    return f"AUC of {model_name} is {auc}"
