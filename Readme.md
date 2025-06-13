
### Build the Docker Image
```bash
docker build -t karunya.edu.laballotment .
```


### Run the Docker Container
```bash
docker run -p 8000:8000 karunya.edu.laballotment
```



#### NGINX reverse proxy and HTTPS:
Meant to be in the host server.

/etc/nginx/conf.d/laballotment.conf:
```nginx
server {
    listen 80;
    server_name laballotment.karunya.edu;
    return 301 https://$server_name;
}
server {
  listen 443 ssl;
  server_name laballotment.karunya.edu;

  ssl_certificate #add the path 
  ssl_certificate_key #add the path

 location / {
  proxy_pass http://0.0.0.0:8000;
  proxy_set_header Host $host;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
  proxy_set_header Accept-Encoding gzip;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_http_version 1.1;
 }
 }
```
