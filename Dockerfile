FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]