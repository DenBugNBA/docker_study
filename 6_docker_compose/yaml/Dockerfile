FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./yaml_parser.py ./yaml_parser.py

CMD [ "python", "./yaml_parser.py" ]
