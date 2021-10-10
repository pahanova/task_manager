FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # dockerize:
    DOCKERIZE_VERSION=v0.6.1 \
    # tini:
    TINI_VERSION=v0.18.0 \
    # poetry:
    POETRY_VERSION=1.0.5 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        bash \
        build-essential \
        curl \
        gettext \
        git \
        libpq-dev \
        wget \
        fontconfig libfreetype6 libjpeg62-turbo libpng16-16 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base \
        libmagic1 \
        python-dev \
        libxml2-dev \
        libxslt1-dev \
        antiword \
        unrtf \
        poppler-utils \
        #    pstotext \
        tesseract-ocr \
        flac \
        ffmpeg \
        lame \
        libmad0 \
        libsox-fmt-mp3 \
        sox \
        libjpeg-dev \
        swig \
        libpulse-dev \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    # Installing `dockerize` utility:
    # https://github.com/jwilder/dockerize
    && wget "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && tar -C /usr/local/bin -xzvf "dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && rm "dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" && dockerize --version \
    # Installing `tini` utility:
    # https://github.com/krallin/tini
    && wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" \
    && chmod +x /usr/local/bin/tini && tini --version \
    # install wkhtmltopdf
    && wget "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.stretch_amd64.deb" \
    && dpkg -i "wkhtmltox_0.12.6-1.stretch_amd64.deb" \
    && rm "wkhtmltox_0.12.6-1.stretch_amd64.deb" && wkhtmltopdf -V \
    # Installing `poetry` package manager:
    # https://github.com/python-poetry/poetry
    && pip install "poetry==$POETRY_VERSION" && poetry --version \
    && sed -i 's/CipherString = DEFAULT@SECLEVEL=2/CipherString = DEFAULT@SECLEVEL=0/g' /etc/ssl/openssl.cnf

WORKDIR /code

# Создание папки под статику и добавление группы и пользователя,
# с которыми будет выаолняться код
RUN mkdir /code/staticfiles \
    && groupadd -r web && useradd -d /code -r -g web web \
    && chown web:web -R /code

COPY --chown=web:web ./poetry.lock ./pyproject.toml /code/

# Устаповка зависимостей с помощью Poetry
# установить NO_DEV в '', если нужны devtools
ARG NO_DEV='--no-dev'
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi ${NO_DEV}

USER web

ENTRYPOINT ["tini", "--"]

COPY --chown=web:web . /code