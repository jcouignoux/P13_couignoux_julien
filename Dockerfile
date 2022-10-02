FROM python:3


# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
# ENV PROJECT_DIR="lettings-site"
# RUN mkdir $PROJECT_DIR
# COPY . $PROJECT_DIR
# WORKDIR $PROJECT_DIR
# RUN pip install -r requirements.txt
# EXPOSE 8000
# ENTRYPOINT ["python", "manage.py", "runserver"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/