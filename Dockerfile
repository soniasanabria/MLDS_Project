FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --upgrade pip \
    && pip install gunicorn
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src\deploymentAPI:app"]



