FROM httpd:alpine

LABEL description="Docker課題:Apacheサーバー(Alpineベース)"


RUN mkdir /usr/local/apache2/conf/include/
RUN echo 'Include conf/include/*.conf ' >> /usr/local/apache2/conf/httpd.conf

COPY ./custom.apache.conf /usr/local/apache2/conf/include/
