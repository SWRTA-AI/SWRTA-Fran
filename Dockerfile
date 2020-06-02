
# Pulling from base Python image
FROM jessinra/swrta-fran-base:latest

# author of file
LABEL maintainer="Jessinra"

# Set the working directory of the docker image
WORKDIR /app
COPY . /app

EXPOSE 5000 

ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 