Test page
-----
1.这是一个flask bootstrap 通过heroku部署的DEMO
2.现在也同时可部署与EC2

Uwsgi Config
-----
uwsgi -x config/my_uwsgiconf.xml --enable-threads
nginx:

>server {
>	listen 80;
>	server_name demo3.jzorrof.info;
>
>	location / {
>		include uwsgi_params;
>		uwsgi_pass 127.0.0.1:3031;
>	}
>}