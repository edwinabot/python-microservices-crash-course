# This md is for documenting the instalation bullshit on all the OSs

## MAC

## Windows

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