FROM python:3.11

WORKDIR /match-score

# requirements.txt kopyalanıp bağımlılıklar kurulur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# flask API'nın kullandığı port
EXPOSE 5000 

# başlatma komutu
CMD ["python", "flaskApı.py"]




