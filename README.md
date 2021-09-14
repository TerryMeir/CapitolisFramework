# CapitolisFramework

Setup for Python:
download the latest python version from: python.org/downloads/

installation:
check the "add python to your path" checkbox 
choose "customize installation" 

check all the checkbox and PIP must be checked

advance options:
add python to env var - check
costomize install location:  c:\python39

Setting up the virtual env:
go to where the python.exe file exist - on terminal	# costomize install location:  c:\python39
on terminal: python.exe --version (to check the current version)
python.exe -m venv %USERPROFILE%\venvs\*project name*	

Activate the vertual env:
go to the project folder: cd %USERPROFILE%\venvs\*project name*
cd Scripts 
avtiavte.bat - activation of the venv
deactiveate - exit the venv

Installing dependencies:
pip install: selenium, pytest, python-dotenv

clone project from git inside %USERPROFILE%\venvs\*project name*
