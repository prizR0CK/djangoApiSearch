FROM ubuntu:latest
LABEL authors="prizrock"
RUN apt-get update -qy
RUN apt-get install -qy python3.11 python3-pip python3.11-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]
