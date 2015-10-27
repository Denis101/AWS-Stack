AWS LAMP Stack
==============
Orchestrate and provision a LAMP stack on AWS with Ansible.

Requires the following environment variables set:
* `AWS_ACCESS_KEY_ID` - Your AWS access key ID.
* `AWS_SECRET_ACCESS_KEY` - Your AWS secret access key.
* `AWS_KEY_PAIR` - Named identifier of your AWS key pair.
* `AWS_KEY_PAIR_PATH` - Local path to the AWS key pair's SSH private key.

Run while in the root directory with:
```
./provision.sh
```

Configuration
-------------
Global application settings can be found in `ansible/roles/common/vars/main.yml`.
This contains the `aws_region`, `db_username`, `db_password`, and `app_name` settings.

---

Very unfinished.
