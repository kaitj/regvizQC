# Use Ubuntu 16.04 LTS
FROM ubuntu:xenial-20180808

MAINTAINER <tkai@uwo.ca>

run mkdir -p /src/install_scripts
COPY ./install_scripts/*.sh /src/install_scripts/

ENV DEBIAN_FRONTEND noninteractive

# Remove install scripts
RUN rm -rf /src
