FROM python:latest

WORKDIR /distributed_systems_project

COPY requirements.txt ./

RUN pip3 install --upgrade pip --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "cmd/app.py" ]
