FROM jenkins/jenkins:lts
MAINTAINER Mauro Franchini

USER root
RUN mkdir /var/cache/jenkins
RUN chown -R jenkins:jenkins /var/cache/jenkins
RUN mkdir /var/log/jenkins
RUN chown -R jenkins:jenkins /var/log/jenkins

USER jenkins

ENV JENKINS_OPTS="--logfile=/var/log/jenkins/jenkins.log --webroot=/var/cache/jenkins/war"
