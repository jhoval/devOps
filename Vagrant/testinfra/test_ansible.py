import requests
import pytest

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running

def test_php_is_installed(host):
    php = host.package("php-fpm")
    assert php.is_installed

def test_php_running(host):
    php = host.service("php-fpm")
    assert php.is_running

def test_url(TestinfraBackend):
  host = TestinfraBackend.get_hostname()
  nginx_response = requests.get("http://" + host + ":8080", verify=False)
  assert nginx_response.status_code == 200

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled
