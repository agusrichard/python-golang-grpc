FROM python:3.8

LABEL agusrichard "agus.richard21@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]