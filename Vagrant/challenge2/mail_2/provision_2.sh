echo -------------------------------------------------
echo
echo SELinux設定
echo
echo ------------------------------------------------
SELINUXTYPE=disabled

echo -------------------------------------------------
echo
echo firewallの設定
echo
echo ------------------------------------------------
#smtp許可
firewall-cmd --add-service=smtp --zone=public --permanent

#imap用のポート許可 143
firewall-cmd --add-port=143/tcp --zone=public --permanent
firewall-cmd --add-port=143/udp --zone=public --permanent

#リロード
firewall-cmd --reload

#確認
#firewall-cmd --list-all --zone=public --permanent


echo -------------------------------------------------
echo
echo Postfixのインストール
echo
echo ------------------------------------------------
sudo yum install -y postfix

#起動
#service postfix start

#自動起動
#chkconfig postfix on

echo -------------------------------------------------
echo
echo Postfixの設定を変更
echo
echo ------------------------------------------------
sudo mv /etc/postfix/main.cf /etc/postfix/main.cf.org
sudo cp /vagrant/mail_2/work/postfix/main.cf /etc/postfix/main.cf

#再起動
#service postfix restart

echo -------------------------------------------------
echo
echo telnetのインストール
echo
echo ------------------------------------------------
yum -y install telnet


echo -------------------------------------------------
echo
echo Dvecotのインストール
echo
echo ------------------------------------------------
yum -y install dovecot

#起動
#service dovecot start

#自動起動
#chkconfig dovecot on

echo -------------------------------------------------
echo
echo Dvecotの設定変更
echo
echo ------------------------------------------------
#dovecot.conf
mv /etc/dovecot/dovecot.conf /etc/dovecot/dovecot.conf.org
cp /vagrant/mail_2/work/dovecot/dovecot.conf /etc/dovecot/dovecot.conf

#10-mail.conf
mv /etc/dovecot/conf.d/10-mail.conf /etc/dovecot/conf.d/10-mail.conf.org
cp /vagrant/mail_2/work/dovecot/10-mail.conf /etc/dovecot/conf.d/10-mail.conf

#10-auth.conf
mv /etc/dovecot/conf.d/10-auth.conf /etc/dovecot/conf.d/10-auth.conf.org
cp /vagrant/mail_2/work/dovecot/10-auth.conf /etc/dovecot/conf.d/10-auth.conf

#10-ssl.conf
mv /etc/dovecot/conf.d/10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf.org
cp /vagrant/mail_2/work/dovecot/10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf

#再起動
#service dovecot restart
