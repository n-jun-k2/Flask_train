#!/bin/sh
cp -rp /etc/mysql/conf.d/temp /etc/mysql/conf.d
/entrypoint.sh mysqld