echo -------------------------------------------------
echo
echo Squidインストール
echo
echo ------------------------------------------------
sudo yum  -y install squid

rm /etc/squid/squid.conf
mv /vagrant/squid/squid.conf /etc/squid/squid.conf
