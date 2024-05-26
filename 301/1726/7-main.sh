#!/bin/sh
service mysql start;

# Reset MySQL pwd
/usr/bin/mysqladmin -u root -p"root" password "root"

rm -rf file.json;
rm -rf dev/file.json;

sleep 1;

echo "DROP USER IF EXISTS 'hbnb_dev'@'localhost';" | mysql -ulocalhost -uroot -proot;
echo "DROP DATABASE IF EXISTS hbnb_dev_db;" | mysql -ulocalhost -uroot -proot;

sleep 1;

echo "CREATE DATABASE IF NOT EXISTS hbnb_dev_db;" | mysql -ulocalhost -uroot -proot;
echo "CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';" | mysql -ulocalhost -uroot -proot;
echo "SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';" | mysql -ulocalhost -uroot -proot;
echo "GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';" | mysql -ulocalhost -uroot -proot;
echo "GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';" | mysql -ulocalhost -uroot -proot;
echo "FLUSH PRIVILEGES;" | mysql -ulocalhost -uroot -proot;

echo 'create Amenity name="Wifi"' | ./console.py ;
