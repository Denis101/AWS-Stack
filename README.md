AWS LAMP Stack
==============
Orchestrate and provision a LAMP stack on AWS with Ansible.

Requires the following environment variables set:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_KEY_PAIR
```

Run with:
```
./provision.sh
```

Configuration
-------------
Global application settings can be found in `ansible/roles/common/vars/main.yml`.
This contains the `aws_region`, `db_username`, `db_password`, and `app_name` settings.

---

Very unfinished.
