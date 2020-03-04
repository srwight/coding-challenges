FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 5001

CMD ["python", "-m", "flask run", '--port=5001', '--host="0.0.0.0"']