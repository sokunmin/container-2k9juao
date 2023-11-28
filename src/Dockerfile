# [1]
FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache git gcc musl-dev
#RUN python -m pip install --upgrade certifi

WORKDIR /app

COPY app/echo.py /app/echo.py
COPY app/test.py /app/test.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -U -r requirements.txt


EXPOSE 5003

CMD ["uvicorn", "echo:app", "--host", "0.0.0.0", "--port", "5003"]

# [2]
#FROM ubuntu:focal
#
#COPY requirements.txt .
#
#RUN apt-get update
#RUN apt-get install -y python3.8 python3.8-distutils python3.8-dev pip git
#RUN pip install -r requirements.txt
## Had to downgrade this package for some reason
#RUN pip install jinja2==3.0.3
#RUN modal token new --source poe
#
#ENTRYPOINT ["tail"]
#CMD["-f", "/dev/null"]