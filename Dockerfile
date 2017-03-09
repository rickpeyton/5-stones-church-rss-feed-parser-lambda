FROM amazonlinux:latest

RUN echo 'alias ll="ls -ltha"' >> ~/.bashrc

RUN yum -y update && \
    yum -y install \
      vim \
      zip

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

ENV APP_HOME /app
RUN mkdir -p $APP_HOME/src/site-package
WORKDIR $APP_HOME

COPY src/requirements.txt $APP_HOME/
RUN pip install --no-deps -t $APP_HOME/src/site-package -r $APP_HOME/requirements.txt
RUN pip install --no-deps -r $APP_HOME/requirements.txt
RUN pip install pytest

ADD . $APP_HOME
