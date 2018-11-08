# Use Ubuntu 16.04 LTS
FROM ubuntu:xenial-20180808

MAINTAINER <tkai@uwo.ca>

run mkdir -p /src/install_scripts
COPY ./install_scripts/*.sh /src/install_scripts/

ENV DEBIAN_FRONTEND noninteractive
RUN bash /src/install_scripts/00_install_basics.sh > log_00_basics
RUN bash /src/install_scripts/10_install_regvizqc.sh > log_10_regvizqc

# Remove install scripts
RUN rm -rf /src
