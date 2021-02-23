# Linux Alpineベース
FROM httpd:alpine

# alpineのupdateとupgrade
RUN apk update
RUN apk upgrade

# ローカルにあるapacheの設定をコンテナ内にコピー、apacheの設定に追加
COPY custom.apache.conf /usr/local/apache2/conf/custom.apache.conf
RUN cat /usr/local/apache2/conf/custom.apache.conf >> /usr/local/apache2/conf/httpd.conf