FROM python:3.12-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0" ]