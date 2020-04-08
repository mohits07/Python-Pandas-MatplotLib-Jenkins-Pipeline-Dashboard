FROM python:3.8.0

RUN mkdir -p /usr/src/app
COPY . /usr/src/app/
COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt


EXPOSE 5002

WORKDIR /usr/src/app

ENTRYPOINT ["python3"]

CMD ["./dashboard2.py"]
