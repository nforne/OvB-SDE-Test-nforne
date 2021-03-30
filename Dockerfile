FROM python:3

WORKDIR /submission

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./sde-test-solution.py" ]