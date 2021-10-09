FROM ubuntu:latest
RUN apt update -y
RUN apt install -y python3-pip python3-dev build-essential
RUN export LANG="en_US.UTF-8" ADMIN_PSWD="simple_pswd"
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["create_admin.py"]
CMD ["run.py"]
EXPOSE 5000

