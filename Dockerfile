FROM python:3.10-alpine3.19

RUN apk update && \
    apk add --no-cache openjdk11-jre curl tar bash && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-v", "--tb=short", "--alluredir=allure-results"]
