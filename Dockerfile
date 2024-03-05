FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["gunicorn", "-b", "0.0.0.0:8888", "app:app", "--timeout", "600"]  