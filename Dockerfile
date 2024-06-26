FROM python:3.11.5

WORKDIR /usr/src/app

RUN apt update && apt install -y \
        firefox-esr

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "./main.py"]
