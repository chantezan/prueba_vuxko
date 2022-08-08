FROM python:3.9-buster
RUN apt-get update && apt-get install -y \
    libcurl4-gnutls-dev \
    librtmp-dev \
    openssl \
    libssl-dev
ENV PYTHONUNBUFFERED 1

# TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install
RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz
RUN cd ..

RUN mkdir /code;
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN mkdir /temp ;
EXPOSE 8005 2222