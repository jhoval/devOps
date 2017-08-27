FROM tomcat:7.0
MAINTAINER Mauro Franchini

RUN sed -i -e "s/<\/tomcat-users>//g" /usr/local/tomcat/conf/tomcat-users.xml
RUN echo '<role rolename="manager-gui"/>'
RUN echo '<user username="deploy" password="J3nk1ns!" roles="manager-script,admin-gui,standard,manager-gui"/>' >> /usr/local/tomcat/conf/tomcat-users.xml
RUN echo "</tomcat-users>" >> /usr/local/tomcat/conf/tomcat-users.xml
