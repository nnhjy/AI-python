# Exercise for Course CS-E4800 Artificial Intelligence at Aalto University

## 0. Tips on installing Python
To add `python` and `py` (install py launcher) as terminal command for the installed python.exe:
1. System environment variable (if you install Python for all users to keep `python` and `py` command work everytime you restart the machine):
"Control Panel\All Control Panel Items\System --> Advanced system settings --> Advanced --> Environmental Variables --> Edit in `Path`" 
    - under "User variables for `administrator_username`" only for the administrator, under "System variables" for all users)
    - on installing python, it is recommended to 1) install `python` and `py launcher` to all users and `add python to PATH` unless you would be fine to find `python` and `py` command not work when restarting the machine.
2. User environment variable (if you install Python for the current user, `python` and `py` command would not work after restart): 
Search `environment variables` in the Windows taskbar --> "Edit environment variable for your account" --> Edit in `Path` under "User variables for `the_current_username`"
3. **Edit in `Path`**: add `X:\directory\to\Python3-x\Scripts` (for the `pip` applications) and `X:\directory\to\Python3-x` (for python.exe)

## 1. Set up Python environment
Get and change current working directory in Python interpreter (terminal)
```python
import os
os.getcwd()
os.chdir('Path/to/directory')
```
### 1.1 Create and delete virtual environment
Create a virtual environment: 

In terminal command-line, type \
`py -m venv env3.10-ai`

to install a virtual environment in folder `env3.10-ai` under the current working directory and based on the Python interpreter to which `py` points.

Delete a virtual environment: \
`rm -r <folder_name_of_the_virtual_environment>`

### 1.2 Activate and decativate virtual environment
In terminal command-line, type `.\env3.10-ai\Scripts\activate`

to *activate* a virtual environment named `env3.10-ai`; 

and simply type `deactivate` 

to *deactivate* current virtual environment. 

### 1.3 Confirm the path to current Python interpreter
`where python` in terminal command-line check the Python interpreter of current virtual environment. Or in the python console
```python
import sys
sys.executable
```

### 1.4 Install packages under virtual environment
Activate a virtual environment in terminal command-line, then type 

`py -m pip install <package_name>`.

Install local package with development mode:

`py -m pip install -e <path>`

Install requirements file:

`py -m pip install -r requirements.txt`

Uninstall packages:

`pip uninstall <package_name>`

### 1.5 Display installed packages under the current environment
Activate a virtual environment in terminal command-line, then type

`pip list`



