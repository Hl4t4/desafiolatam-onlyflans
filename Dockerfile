FROM python:3.12.4-alpine3.20

# Set working directory


WORKDIR /usr/onlyflans

# New User
RUN adduser -D hlata

# Copy data
COPY ./requirements.txt ./
COPY ./startcmd.sh ./
COPY ./onlyflans/ ./

# Update Linux and install dependencies
RUN apk update && apk upgrade && apk add --no-cache make g++ openssh bind-tools curl

# Install pip packages
RUN pip install -r requirements.txt

# Static files here because it need permissions to create the files
RUN python manage.py collectstatic --noinput

# Expose the listening port
EXPOSE 80

# Change user
USER hlata

# Launch app
CMD sh /usr/onlyflans/startcmd.sh
