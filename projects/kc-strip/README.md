
## Agoric Node Upgrade Plays

 - ping.yml
 - ag-update.yml - WARNING! deletes all state
 - ag-config.yml

## Ansible cheat-sheet

To start, let's run `plays/ping.yml` to check connectivity with the
node. The naive approach doesn't quite work:

```
$ ansible-playbook plays/ping.yml
[WARNING]: provided hosts list is empty
```

Specifying an inventory gets us closer:

```
$ ansible-playbook --inventory=.../inventory.yml  plays/ping.yml
FAILED! => {"msg": "... undefined variable ..."}
```

Our inventory refers to some variables kept in a vault:

```
$ ansible-playbook --ask-vault-pass --inventory=.../inventory.yml  plays/ping.yml
TASK [ping] *******
ok: [204...]
```
