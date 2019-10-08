# Dockerfile

FROM python:3.7

RUN pip install --upgrade google-cloud-bigquery
RUN pip install google-cloud
RUN pip install requests
RUN pip install google-auth
RUN pip install flask
RUN pip install pandas
WORKDIR /test20

ENTRYPOINT ["python"]
COPY . /test20

CMD ["main.py"]
