FROM gitpod/workspace-full:latest
USER root
RUN apt-get update \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash \
    && apt-get install -yq libmpc-dev libmpfr-dev libgmp-dev flex git-lfs libnl-3-dev libnl-genl-3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
