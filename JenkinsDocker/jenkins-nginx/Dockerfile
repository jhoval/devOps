FROM nginx
MAINTAINER Mauro Franchini

RUN rm /etc/nginx/conf.d/default.conf

COPY conf/jenkins.conf /etc/nginx/conf.d/jenkins.conf
COPY conf/tomcat.conf /etc/nginx/conf.d/tomcat.conf
COPY conf/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 8080

CMD ["nginx"]
