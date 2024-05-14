# workaround s.t. we don't have to rebuild the whole image
FROM r8.im/daanelson/minigpt-4

COPY minigpt4/configs/models/minigpt4.yaml /src/minigpt4/configs/models/minigpt4.yaml
COPY minigpt4/models/mini_gpt4.py /src/minigpt4/models/mini_gpt4.py

RUN curl -o /usr/local/bin/pget -L "https://github.com/replicate/pget/releases/download/v0.8.1/pget_$(uname -s)_$(uname -m)" && chmod +x /usr/local/bin/pget