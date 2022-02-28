FROM python:3

RUN apt-get update -qq

RUN apt-get install -y python3-pip
RUN apt-get install -y vim
RUN pip install pytest 
RUN pip install sympy 
RUN pip install numpy
RUN pip install anytree
RUN pip install pipenv
RUN mkdir /DailyCodingChallenge
COPY ./*.py /DailyCodingChallenge
COPY ./run.sh /DailyCodingChallenge
COPY ./Pipfile.lock /DailyCodingChallenge
RUN chmod +x /DailyCodingChallenge/run.sh
RUN echo 'HTML_REPORT_PATH="./test_reports"' >> /DailyCodingChallenge/.env

RUN pipenv install html-testrunner
RUN pipenv install pytest-html 
RUN pipenv install pytest
RUN pipenv install numpy
RUN pipenv install 
#RUN pipenv shell


WORKDIR /DailyCodingChallenge

CMD [ "pytest", "./code*.py" && "/bin/bash" ]
