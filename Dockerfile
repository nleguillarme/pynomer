# pynomer (https://github.com/nleguillarme/pynomer)

FROM openjdk:8
COPY --from=python:3.7-alpine / /

RUN apk --no-cache add sudo curl bash

RUN sudo sh -c '(echo "#!/usr/bin/env sh" && curl -L https://github.com/globalbioticinteractions/nomer/releases/download/0.1.22/nomer.jar) > /usr/local/bin/nomer && chmod +x /usr/local/bin/nomer' && nomer version
# COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install pynomer

#ENTRYPOINT [ "python3" ]

CMD [ "pynomer", "version" ]
