# Build stage for Free5GC
FROM golang:1.23.1-bullseye AS builder
LABEL maintainer="Yathusan"

# Install dependencies for building Free5GC
RUN apt-get update \
    && apt-get -y install gcc cmake autoconf libtool pkg-config libmnl-dev libyaml-dev apt-transport-https ca-certificates \
    && curl -sL https://deb.nodesource.com/setup_20.x | bash - \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y nodejs yarn \
    && apt-get clean

# Get and build Free5GC
RUN cd $GOPATH/src \
    && git clone --recursive -j `nproc` https://github.com/yathy1040/free5gc.git \
    && cd free5gc \
    && make all

# Final stage based on Ubuntu 20.04
FROM ubuntu:20.04
LABEL maintainer="Yathusan"
LABEL description="Free5GC v3.4.3"
ENV DEBIAN_FRONTEND=noninteractive

# Install runtime dependencies
RUN apt-get update \
    && apt-get -y install vim net-tools curl libmnl0 libyaml-0-2 iproute2 iptables tcpdump iputils-ping \
    && apt-get clean

WORKDIR /free5gc
RUN mkdir -p config/ log/ config/TLS/ public/

# Copy artifacts from builder stage
COPY --from=builder /go/src/free5gc/bin/* ./
COPY --from=builder /go/src/free5gc/webconsole/bin/webconsole ./webui
COPY --from=builder /go/src/free5gc/webconsole/public ./public
COPY --from=builder /go/src/free5gc/config/* ./config/

VOLUME [ "/free5gc/config"]

# Expose necessary ports
EXPOSE 8000 5000
