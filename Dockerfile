FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip intsall --no-cache-dir -e .

EXPOSE 5000

ENV FLASK_APP = application.py

CMD ["python" , "application,py"]