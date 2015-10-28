#!/usr/bin/env python
import sys
import getopt
import os
import yaml

from ansible.playbook import PlayBook
from ansible import callbacks
from ansible import utils
from ansible import inventory
from ansible import errors
from ansible.callbacks import display

def run_playbook(path, inv_path, pk):
    inv = inventory.Inventory(inv_path)
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    pb = PlayBook(
        playbook=path,
        inventory=inv,
        private_key_file=pk,
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        stats=stats
    )

    try:
        pb.run()

        playbook_cb.on_stats(pb.stats)
    except errors.AnsibleError, e:
        display("ERROR: %s" % e, color='red')
        return 1

    return 0

def orchestrate():
    return run_playbook('ansible/orchestrate.yml', 'ansible/hosts')

def provision(pk):
    return run_playbook('ansible/app.yml', 'ansible/roles/appserver/hosts', pk)

def main(argv):
    conf = ''
    conf_contents = object()
    pk = ''

    try:
        opts, args = getopt.getopt(argv, "pc", ["private_key_file=", "config="])
    except getopt.GetoptError:
        print 'provision.py error'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--private-key-file'):
            pk = arg
        elif opt in ('-c', '--config'):
            conf = arg

    if conf:
        with open(conf, 'r') as stream:
            conf_contents = yaml.load(stream)

    if not pk:
        if conf_contents.private_key_file:
            pk = conf_contents.private_key_file
        else
            pk = os.environ['AWS_KEY_PAIR_PATH']
            
    provision(pk)

if __name__ == "__main__":
    display(" ", log_only=True)
    display(" ".join(sys.argv), log_only=True)
    display(" ", log_only=True)

    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt, ke:
        display("ERROR: interrupted", color='red', stderr=True)
        sys.exit(1)
