sudo yum -y install httpd

sudo yum -y remove mariadb-libs

sudo yum -y localinstall http://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm $
sudo yum -y install mysql-community-server

sudo yum -y install php

sudo yum -y install wget
wget http://ja.wordpress.org/latest-ja.tar.gz
tar zxvf latest-ja.tar.gz