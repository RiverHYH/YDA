import importlib.util
import sys

def install_and_import(package, top_level_module_name, short_name):
    import subprocess
    cmd = [sys.executable, "-m", "pip", "install", package]
    print(f"Running command: {cmd}")
    subprocess.check_call(cmd)
    globals()[short_name] = importlib.import_module(top_level_module_name)

packages = {"pandas": ["pandas", "pd"], "numpy": ["numpy", "np"], "scikit-learn": ["sklearn", "sklearn"], "matplotlib": ["matplotlib", "plt"], "seaborn": ["seaborn", "sns"]}

for package, (top_level_module_name, short_name) in packages.items():
    if importlib.util.find_spec(top_level_module_name) is None:
        user_input = input(f"{package} is not installed. Do you want to install it? (y/n)")
        if user_input.lower() == 'y':
            print(f"Installing {package}...")
            install_and_import(package, top_level_module_name, short_name)
            print(f"{package} installed!")
        else:
            print(f"Installation ceased! Thank you!")
    else:
        print(f"{package} module is imported as {short_name}")
        globals()[short_name] = importlib.import_module(top_level_module_name)
        
        
        
        
        
        
        
def BreakPoint():
    flag=input("Break the Program: (True/False)")
    if flag=="True":
        raise Exception("Breakpoint Initiated")
    else:
        pass
