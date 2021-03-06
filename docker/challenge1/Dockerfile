# ベースのDockerイメージを指定
FROM alpine:latest

# apache2をインストール
RUN apk add --no-cache apache2

# custom.apache.confをコピー
COPY custom.apache.conf /etc/apache2/conf.d/custom.apache.conf

# httpdをフォアグラウンドで起動
CMD ["/usr/sbin/httpd","-DFOREGROUND"]