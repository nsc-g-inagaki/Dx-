FROM alpine:latest
RUN apk add apache2
COPY custom.apache.conf /etc/apache2/conf.d/custom.apache.conf
CMD ["/usr/sbin/httpd","-DFOREGROUND"]