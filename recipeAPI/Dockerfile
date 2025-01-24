FROM python:3.11

WORKDIR /code

COPY recipeAPI/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY recipeAPI/ .

CMD ["fastapi", "run", "main.py", "--port", "8001"]