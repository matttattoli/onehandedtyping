# Onehandedtyping

## Disclaimer
Idea completely from [veryjos](https://github.com/veryjos/onehandedtyping), but for Windows.

## OS Support
This will only work for Windows as the keyboard library is only capable of canceling key press
events for windows. If you need Linux support, check out
[veryjos/onehandedtyping](https://github.com/veryjos/onehandedtyping).

## Getting Started
You can use the config as is. After installing python 3.7 and the required packages, you can run
`py main.py`.

If you want this to run at startup, you can run the `install.bat` script to have it copied into your
user's startup folder. The script copies the main.py as a pyw so it does not require an open command
prompt, copies the remap configuration file to your userprofile folder, and installs the pip
packages.
