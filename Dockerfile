FROM python:3.12  
 
RUN mkdir /app
WORKDIR /app
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
RUN apt-get update -y
RUN apt-get install python3-dev libldap2-dev libsasl2-dev -y 
RUN pip install --upgrade pip 
COPY requirements.txt  /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
EXPOSE 8000 

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
