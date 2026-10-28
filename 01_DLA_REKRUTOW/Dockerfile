FROM ros:jazzy

RUN apt-get update && apt-get install -y \
    python3-serial \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
