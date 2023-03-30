FROM python:3.6

RUN pip install jenkins

WORKDIR /app

COPY app.py .

CMD ["python"]
