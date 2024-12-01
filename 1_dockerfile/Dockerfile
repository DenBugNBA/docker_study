FROM ubuntu:20.04

RUN apt-get update && apt-get install -y vim wget curl git

WORKDIR /home/denis

# /home/denis/script.sh
COPY ./script.sh ./script.sh

RUN touch hello.sh && echo "echo 'Hello from container'" > hello.sh

# Uses "robbyrussell" theme (original Oh My Zsh theme), with no plugins
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)" -- \
    -t robbyrussell \
    -p https://github.com/zsh-users/zsh-autosuggestions

ENV ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#dedede,bg=#9c9c9c,bold,underline"

ENTRYPOINT ["zsh"]

CMD ["hello.sh"]
