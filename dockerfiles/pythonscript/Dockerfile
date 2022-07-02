FROM python:3.9-slim-buster
COPY ./get_data.py .
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 get_data.py