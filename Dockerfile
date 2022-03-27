ARG APP_DIR="/tmp"

FROM python:3.8

ARG APP_DIR
WORKDIR ${APP_DIR}

# Install python packages
RUN pip install 'poetry==1.1.4'
COPY poetry.lock pyproject.toml ${APP_DIR}/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy function code
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:${APP_DIR}"

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]
