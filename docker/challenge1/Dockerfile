#最新状態のalpine指定
FROM alpine:latest
#Apacheインストール
RUN apk update && apk --no-cache add apache2
#Apache設定
COPY ./*.conf /etc/apache2/conf.d/
#htmlフォルダのコピー
COPY ./html /var/www/html
#Apache起動
CMD [ "/usr/sbin/httpd" ,"-DFOREGROUND"] 