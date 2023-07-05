def SetEnv():
    import os
    try:
        import pandas as pd
        print("pandas is imported")
    except ImportError:
        Flag=input("pandas is not installed.Input 'True' to install, else quit")
        if Flag=="True":
            os.system('pip install pandas')
            import pandas as pd
            print("pandas is imported")
        else:
            pass
    
    try:
        import numpy as np
        print("numpy is imported")
    except ImportError:
        Flag=input("numpy is not installed.Input 'True' to install, else quit")
        if Flag=="True":
            os.system('pip install numpy')
            import np
            print("pandas is imported")
        else:
            pass
    try:
        import sklearn
        print("sklearn is imported")
    except ImportError:
        Flag=input("sklearn is not installed.Input 'True' to install, else quit")
        if Flag=="True":
            os.system('pip install -U scikit-learn')
            import sklearn
            print("sklearn is imported")
        else:
            pass
        
    
    try:
        import matplotlib.pyplot as plt
        print("matplotlib is imported")
    except ImportError:
        Flag=input("matplotlib is not installed.Input 'True' to install, else quit")
        if Flag=="True":
            os.system('pip install matplotlib')
            import matplotlib.pyplot as plt
            print("matplotlib is imported")
        else:
            pass
    
    try:
        import seaborn as sns
        print("seaborn is imported")
    except ImportError:
        Flag=input("seaborn is not installed.Input 'True' to install, else quit")
        if Flag=="True":
            os.system('pip install seaborn')
            import seaborn as sns
            print("seaborn is imported")
        else:
            pass
    
def BreakPoint():
    flag=input("Break the Program: (True/False)")
    if flag=="True":
        raise Exception("Breakpoint Initiated")
    else:
        pass