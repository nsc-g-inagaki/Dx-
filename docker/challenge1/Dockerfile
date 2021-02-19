FROM alpine:latest
RUN apk add apache2
COPY custom.apache.conf /etc/apache2/conf.d/
EXPOSE 80
CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["httpd"]
