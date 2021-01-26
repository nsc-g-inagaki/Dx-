# apacheを作成するのに使うイメージ
FROM httpd:alpine

# alpineのupdateとupgradeを実行
RUN apk update; 
RUN apk upgrade;

# apacheの設定をコンテナ内にコピー
COPY custom.apache.conf /usr/local/apache2/conf/custom.apache.conf

# コピーした設定をApacheの設定に追加
RUN echo "include /usr/local/apache2/conf/custom.apache.conf" >> /usr/local/apache2/conf/httpd.conf