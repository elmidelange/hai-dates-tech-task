ARG APP_DIR="/tmp"

FROM python:3.8

ARG FUNCTION_DIR

# Install python packages
RUN pip install 'poetry==1.1.4'
COPY poetry.lock pyproject.toml ${FUNCTION_DIR}/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy function code
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:${FUNCTION_DIR}"

CMD [ "poetry", "python", "main.py" ]
