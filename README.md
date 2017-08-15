This is the devOps training repository.

**Step 1**
Run `vagrant up` inside _Vagrant_ directory.

**Step 2**
Run `ansible-playbook -i vagrantInventory ./provisioning/playbook.yml` 

:warning: _If you are behind a proxy, please uncomment the "configure proxy" section inside Vagrantfile_ :warning:

> Now if you go in your browser to 127.0.0.1:2222 you can see the last step of installing wordpress

**Step 3**
To test the infra, I used [TestInfra](https://testinfra.readthedocs.io/), with the following file: [test_ansible.py](Vagrant/testinfra/test_ansible.py)
