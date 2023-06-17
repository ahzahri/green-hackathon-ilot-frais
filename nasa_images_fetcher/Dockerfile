# Python 3.11.3 with pip in this base image
FROM python:3.9.17-alpine3.18

# install bash
RUN apk add --no-cache bash

RUN apk update

# upgrade pip
RUN python -m ensurepip --upgrade

# create a non-root user
RUN adduser -D images_fetcher
USER images_fetcher

# set the working directory
WORKDIR /home/images_fetcher/app

# copying the application with the correct permissions
COPY --chown=images_fetcher . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 