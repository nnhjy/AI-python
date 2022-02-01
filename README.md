# Exercise for Course CS-E4800 Artificial Intelligence at Aalto University

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



