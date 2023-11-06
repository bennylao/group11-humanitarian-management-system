# COMP0066_Humanitarian_Management_System

This application is created by Group 11.

%description% blablabla

The application can be run without installation. However, it is recommended to install it.
After installation, the application can be accessed in any directory at anytime with the command:
```shell
hmsGroup11
```

## Installation Guide

### Double-click Installation
- Windows

Windows users can install the application via double-click on ```Installation_Win.bat```.

- Mac

Mac users can install the application via double-click on ```Installation_Mac.applescript```,
and Press ```▶ (Run the Script)```.

If the installation could not work properly, you can install it manually through Terminal/CMD/PowerShell:

### Manual Installation

Before manual installation, user has to copy the absolute path to the project directory 
***COMP0066_Humanitarian_Management_System***:

- On windows:
Open File Explorer and navigate to the directory contains the application package, 
right-click on the package and select ```copy as path```

- On Mac:
Open Finder and navigate to the directory contains the application package, 
while holding ```option```, right-click on the package and select ```Copy "pkg" as Pathname```

After copying the absolute path,
open ```Terminal``` on Mac, or ```PowerShell```/```Command Prompt``` on Windows, then run the following pip command:
(```{local/path/to/package}``` is the path you copied in the previous step)
```shell
pip install {local/path/to/package}
```

## To launch the application

Once the application is installed, the application can be run at anytime by 
executing the following command on Terminal or Command Prompt:
```shell
hmsGroup11
```


## Notes for Developers

Before configuration, it is recommended to create a ***virtual environment*** and 
install dependencies only in the virtual environment.

To install dependencies, run the command below in terminal with activated venv:
```shell
pip install -r requirements.txt
```
