FROM python:3.12-slim

ENV TZ="America/Los_Angeles"

WORKDIR /backend

COPY ./requirments.txt /backend/requirments.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirments.txt

COPY ./app /backend/app

EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
