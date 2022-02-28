# Solutions for Daily Coding Challenge

Sign up for an account at <a href>"https://dailycodingproblem.com"</a> to automatically receive  a daily coding problem in your mail box.


This repository contains continuous update of my solutions (code snippets).  I try to keep it a consistent activity as a way to keep my mind entertained.  

## Coding Practice
Problem descriptions are here to require understanding before moving ahead!

Comments are here to explain code to other programmers, better yet, as notes to my future self.
The comment section contains date, problem's description follows by my thought on computation flow and pseudo code.

Codes are here to explain algorithms to the computer.
The code section usually contains function(s) for addressing the main problem and test_func() written for pytest module.
In order to optimize, we first take measurement.  Some solutions here also output elapsed runtime if there are multiple 
ways to implement a solution.

Often, I would recommit updates on individual file with further thoughts, improvement or total rewrite of the solution.


## How to Run

** 1.  Install pytest (pip install  pytest)

** 2.  git clone https://github.com/hurricanemark/DailyCodingChallenge.git

** 3.  Run pytest (pytest ./*.py)

**     or, execute individual python solution (python codechalleng-##.py)

**     or, execute python tests.py for comprehensive testing of the whole directory

**     or, python3 module_unittests.py

**     PIPENV: using provided Pipfile.lock

```
pipenv install
pipenv shell
pipenv run python ./tests.py
exit()
```



## Run Using Docker Image
=======
## Develop && Run Tests Using Docker Image

Install docker-ce on your local machine.  Follow this link [**docker-ce**](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1) for installation instruction.  
Make sure you have .dockerignore file in your folder.

$ docker build . -t pydockerrunner

$ docker rm runmycodechallenges; docker run -it --name runmycodechallenges pydockerrunner:latest "/bin/bash"


## Organization

One problem/solution per python file.
Each python file contains the given problem in the commented section and my attempted code below it.  The files are not linked or referenced to one another.  However, you could import each one as module (see module_unittests.py) or run pytest on the entire directory (see tests.py).  Be sure to open it up and read it.  

Feel free to suggest better performance for any of my solution here.


Published URL: https://hurricanemark.github.io/DailyCodingChallenge/
