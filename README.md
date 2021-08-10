# Python Bootcamp (NuCamp)

### A living repo of work based on the curriculum of NuCamp's new Python Bootcamp

#### notes:

Windows Setup:
- Install Git for Windows [Git for Windows](https://git-scm.com/downloads)
- Install Python [Python 3.9.4](https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe)(make sure to tick the boxes for Adding Python to PATH and then Disabling the path length limit after installation is successful)

- Install Python VS Code Extension 
- Install pip, pylint, and pep8
- After everything is installed, open a terminal and run each command one at a time.
```bash
python -m pip install --upgrade pip
pip install pylint
pip install --upgrade autopep8
```
- Last step is add this to the very end of your settings.json in VS Code(***after*** the second to last closing bracket)
```javascript
"editor.formatOnSave": true,
"python.linting.enabled": true,
"python.linting.pylintEnabled": true
```