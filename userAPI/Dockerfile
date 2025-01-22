FROM python:3.11-slim

WORKDIR /code

COPY userAPI/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY userAPI/ .

CMD ["fastapi", "run", "main.py", "--port", "8000"]