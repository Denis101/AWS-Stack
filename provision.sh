cd ~/Repositories/super6-aws/

echo "Orchestrating environment"
ansible-playbook -i ansible/hosts ansible/orchestrate.yml

echo "Provisioning webservers"
ansible-playbook -i ansible/roles/appserver/hosts/ec2.py ansible/app.yml
