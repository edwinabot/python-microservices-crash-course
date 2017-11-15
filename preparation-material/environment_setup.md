# Here is the environment setup for this workshop

We will be using [Visual Studio Code](https://code.visualstudio.com/) for coding and we should install [this great extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Python

## MAC

Download latest python 3.6 PKG file from: https://www.python.org/downloads/mac-osx/
Make sure to select "Add python to the PATH" option.

```
cd python-microservices-crash-course
pip install -r requirements.txt
```

## Windows

Download MSI installer from https://www.python.org/downloads/windows/
Make sure to select "Add python to the PATH" on the installer first dialog.

Open a terminal (Start menu > Run) then type cmd and press enter.

Run following command to install dependencies:

```
cd python-microservices-crash-course
pip install -r requirements.txt
```

## Ubuntu / Debian

First we must install Python 3.6

```Bash
$ sudo apt-get update
$ sudo apt-get install python3.6
$ sudo pip3 install virtualenv
```

> Note: debian users might need to add testing repos, [check this](https://unix.stackexchange.com/questions/332641/how-to-install-python-3-6).

Later you should clone the [repo for the workshop](https://github.com/edwinabot/python-microservices-crash-course.git) and then do this

```Bash
$ cd python-microservices-crash-course
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# So... what have I done?

You just instaled Python 3 cloned the repo for the workshop, then created a virtualenv, you activated the virtualenv and then you installed all the dependencies for the app.
