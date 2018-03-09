upstream todolist {
        server django_server:8888;
}



server {
        server_name todo.ru;
        listen 80;

        location / {
                proxy_pass http://todolist;
        }

        location /api/ {
                proxy_pass http://todolist;
        }

        location /static/ {
                alias /usr/share/nginx/html/static/;
        }

        #access_log /usr/share/nginx/logs/;
        #error_log  /usr/share/nginx/logs/;
}
