
# Run this from the root folder!

echo "Orchestrating environment"
ansible-playbook -i ansible/hosts ansible/orchestrate.yml

echo "Provisioning webservers"
ansible-playbook -i ansible/roles/appserver/hosts/ec2.py --private-key=$AWS_KEY_PAIR_PATH ansible/app.yml
