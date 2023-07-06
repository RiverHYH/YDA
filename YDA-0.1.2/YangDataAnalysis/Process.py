def MinMaxNormaliser(Array):#Normalise the numeric values into floats using Min_Max method
    Normalised_Array=[]
    Min=min(Array)
    Max=max(Array)
    for i in Array:
        Normalised_Value=(i-Min)/(Max-Min)
        Normalised_Array.append(Normalised_Value)
    return Normalised_Array


def GetTrainTime(Model,x_train,y_train):#This function can calculate the training time of a model and returns a trained model
    import time
    start=time.time()
    Model.fit(x_train,y_train)
    end=time.time()
    model_name=str(type(Model)).split('.')[-1].split('’')[0][:-2]
    print(f"Training Time of {model_name} is {round(end-start,4)} seconds")
    return Model

def GetNilCount(df,plot=False,threshold=0.6,width=20):
    import pandas as pd
    Columns=df.columns.values.tolist()
    MissingValuePerC=[]
    for i in Columns:
        MissingValuePerC.append(df[i].isna().sum()/len(df[i]))
    MissingList=pd.DataFrame({"Features":Columns,"%MissingValues":MissingValuePerC})
    if not plot:
        return MissingList
    else:
        import seaborn as sns
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(width, 6))
        ax = sns.barplot(x='Features', y='%MissingValues', data=MissingList)
        ax.axhline(threshold, ls='--', color='red')
        ax.set_ylim(0,0.99)

        plt.show()