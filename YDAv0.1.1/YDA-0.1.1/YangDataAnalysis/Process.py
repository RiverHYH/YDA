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