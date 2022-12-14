FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
copy . . 
COPY Scores.txt /Scores.txt

CMD [ "python", "./MainGame.py" ]

