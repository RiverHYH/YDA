import importlib.util
import sys

def install_and_import(package):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    globals()[package] = importlib.import_module(package)

packages = {"pandas": "pd", "numpy": "np", "sklearn": "sklearn", "matplotlib": "plt", "seaborn": "sns"}

for package, short_name in packages.items():
    if importlib.util.find_spec(package) is None:
        user_input = input(f"{package} is not installed.Do you want to install it?(y/n)")
        if user_input.lower() == 'y':
            print(f"Installing {package}...")
            install_and_import(package)
            print(f"{package} installed!")
        else:
            print(f"Installation Ceased! Thank You!")
    else:
        print(f"{package} module is imported as {short_name}")
        globals()[short_name] = importlib.import_module(package)
        
        
        
        
        
        
        
def BreakPoint():
    flag=input("Break the Program: (True/False)")
    if flag=="True":
        raise Exception("Breakpoint Initiated")
    else:
        pass