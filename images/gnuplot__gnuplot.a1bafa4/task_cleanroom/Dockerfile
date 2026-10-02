# programbench/gnuplot_1776_gnuplot.a1bafa4:task_cleanroom_v6
# Inference (agent) image and default evaluation image. Build context: repository root.
#   docker build -t programbench/gnuplot_1776_gnuplot.a1bafa4:task_cleanroom_v6 \
#     -f images/gnuplot__gnuplot.a1bafa4/task_cleanroom/Dockerfile .
# /workspace holds only the reference binary and user documentation: no source code.
# The agent must run with no network (docker run --network none ...).
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive LC_ALL=C.UTF-8 LANG=C.UTF-8
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential cmake pkg-config git ca-certificates patch \
      autoconf automake libtool bison zlib1g-dev \
      golang-go rustc cargo python3 python3-pytest python3-venv nodejs \
    && rm -rf /var/lib/apt/lists/*
COPY images/gnuplot__gnuplot.a1bafa4/task_cleanroom/workspace/ /workspace/
RUN chmod +x /workspace/gnuplot
WORKDIR /workspace
