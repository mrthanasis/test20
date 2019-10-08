# Dockerfile
FROM python:3.7

RUN pip install -r requirements.txt
RUN pip install --upgrade google-cloud-bigquery
RUN pip install --upgrade google-cloud-bigquery
RUN pip install google-cloud
RUN pip install requests
RUN pip install google-auth
RUN pip install flask
RUN pip install pandas
ENTRYPOINT ["python"]
CMD ["main.py"]

