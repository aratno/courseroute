# Help!
This is a quick FAQ for people new to the codebase. It will be ammended as
necessary. If there's anything you'd like added, let me know.

### How do I get started?
First, clone the repostiory. Then, make sure Python 3, pip, and virtualenv are
be installed. To create a virtualenv, run:
```
$ virtualenv venv -p python3
```
To start using it, run:
```
$ source venv/bin/activate
```
On completion, this should prepend `(venv)` to your prompt. To install the
dependencies, run:
```
(venv) $ pip install -r requirements.txt
```
This will install each of the dependencies, as described in the requirements
file, to your environment.  
Once these steps are complete, run `main.py`, open your web browser, and go to
`http://127.0.0.1:5000/`. To terminate the program, press CTRL+C.

