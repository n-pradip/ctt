FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN mkdir /app/requirements
COPY requirements/* /app/requirements/
RUN pip3 install -r /app/requirements/base.txt

COPY . /app

#CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]
