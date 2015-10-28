AWS LAMP Stack
==============
Orchestrate and provision a LAMP stack on AWS with Ansible.

Prerequisites
-------------
Requires the following environment variables set:
* `AWS_ACCESS_KEY_ID` - Your AWS access key ID.
* `AWS_SECRET_ACCESS_KEY` - Your AWS secret access key.
* (Optional) `AWS_KEY_PAIR` - Named identifier of your AWS key pair.
* (Optional) `AWS_KEY_PAIR_PATH` - Local path to the AWS key pair's SSH private key.

Running
-------
Run while in the root directory with:
```
./provision.py
```

The following arguments can be passed into the script:
* `-p` or `--private-key-file`. Sets the SSH private key file to use for connecting to instances.
* `-c` or `--config`. Sets the location of the global configuration file. More details about this file can be found in the Configuration section.

Configuration
-------------
The `provision.py` script can read a YAML file with the following structure
```
database:
  username:
  password:

aws:
  access_key:
  secret_key:

git:
  repository:

app:
  name:
  root:
  environment:
```

---

Very unfinished.
