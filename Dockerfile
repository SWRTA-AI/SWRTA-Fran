
# Pulling from base Python image
FROM python:3.8-slim

# author of file
LABEL maintainer="Jessinra"

# Set the working directory of the docker image
WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip
# RUN pip install numpy scipy

# packages that we need
RUN pip install -r requirements.txt 

EXPOSE 5000 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 