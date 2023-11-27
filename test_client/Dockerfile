FROM python:3.8-slim

#RUN python -m pip install --upgrade certifi

RUN pip install requests
WORKDIR /app

ADD ./client.py /app/client.py

CMD ["python", "client.py"]
