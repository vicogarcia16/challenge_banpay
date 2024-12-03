FROM python:3.11

WORKDIR /challenge_banpay

COPY ./requirements.txt /challenge_banpay/requirements.txt

RUN pip install -r requirements.txt 

COPY . .

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]