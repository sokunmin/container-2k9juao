# syntax=docker/dockerfile:1
FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache git gcc musl-dev ssh-askpass
WORKDIR /app

COPY app/echo.py /app/echo.py
COPY app/test.py /app/test.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -U -r requirements.txt


#EXPOSE 5003

#ENTRYPOINT ["tail"]
#CMD ["-f", "/dev/null"]

CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "5000"]

