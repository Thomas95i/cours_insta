FROM python:3.6-buster
COPY . /usr/src/api/
WORKDIR /usr/src/api/
RUN pip3 install pipenv
RUN pipenv install
EXPOSE 5000
CMD [ "pipenv", "run", "python", "run_hw.py" ]