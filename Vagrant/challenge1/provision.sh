echo -------------------------------------------------
echo
echo Apacheインストール
echo
echo ------------------------------------------------
sudo yum -y install httpd


echo -------------------------------------------------
echo
echo MySQLインストール
echo
echo ------------------------------------------------
sudo yum -y remove mariadb-libs
#sudo yum -y localinstall http://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
sudo yum -y localinstall /vagrant/mysql/mysql80-community-release-el7-3.noarch.rpm
sudo yum -y install mysql-community-server


echo -------------------------------------------------
echo
echo PHPインストール
echo
echo ------------------------------------------------
sudo yum -y install php

echo -------------------------------------------------
echo
echo WordPressインストール
echo
echo ------------------------------------------------
sudo yum -y install wget
wget http://ja.wordpress.org/latest-ja.tar.gz
tar zxvf latest-ja.tar.gz
rm latest-ja.tar.gz
