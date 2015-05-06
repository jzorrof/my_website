Test page
-----
1. 这是一个flask bootstrap 通过heroku部署的DEMO
2. 现在也可部署于EC2

Heroku Config
-----
web: gunicorn mywebsite:app

EC2
----

1. Uwsgi Config:<br>
uwsgi -x config/my_uwsgiconf.xml --enable-threads

2. nginx:<br>

>server {
>	listen 80;
>	server_name [domain];
>
>	location / {<br>
>		include uwsgi_params;<br>
>		uwsgi_pass [ip]:[port];<br>
>	}
>}