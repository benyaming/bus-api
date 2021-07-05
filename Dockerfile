FROM python:3.7

RUN pip install pipenv
WORKDIR /home/app
COPY . .
WORKDIR /home/app/israel_transport_api
RUN pipenv install
ENV PYTHONPATH=/home/app
ENV DOCKER_MODE=true
EXPOSE 8000
CMD ["pipenv", "run", "python", "main.py"]
