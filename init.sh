sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm -f /etc/gunicorn.d/*
sudo ln -s /home/box/web/etc/ask.conf.py /etc/gunicorn.d/ask.conf.py
sudo ln -s /home/box/web/etc/hello.conf.py /etc/gunicorn.d/hello.conf.py
sudo /etc/init.d/gunicorn restart
sudo ﻿/etc/init.d/mysql start﻿
