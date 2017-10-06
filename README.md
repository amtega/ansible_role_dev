# Ansible environment role

This is an [Ansible](http://www.ansible.com) role which manages device special files.

## Requirements

- Ansible >= 2.4

## Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

## Filters

The role provides these filters to manipulate the provided presets:

- dev_expand: allows to use placeholders in the special files definition. See samples below.
- dev_to: allows to create a range of numbers. See samples below.

## Dependencies

None.

## Example Playbook

This is an example playbook tall will create loop devices from `/dev/loop0` to `/dev/loop10` and delete devices from `/dev/loop11` to `/dev/loop13`:

```yaml
---
- hosts: all
  roles:
    - dev
  vars:
    loop_device_pattern_present:
      state: present
      path: "/dev/loop{n}"
      type: block
      major: 7
      minor: "{n}"
      mode: "0660"

    loop_device_pattern_absent:
      state: absent
      path: "/dev/loop{n}"

    dev_special_files: >-
      {{ loop_device_pattern_present | dev_expand(n=0 | dev_to (10)) }}
      + {{ loop_device_pattern_absent | dev_expand(n=11 | dev_to (13)) }}
```

## Testing

Test are based on docker containers. You can run the tests with the following commands:

```shell
$ cd dev/test
$ ansible-playbook main.yml
```

If you have docker engine configured you can avoid running dependant 'docker_engine' role (that usually requries root privileges) with the following commands:

```shell
$ cd dev/test
$ ansible-playbook --skip-tags "role::docker_engine" main.yml
```

## License

Not defined.

## Author Information

- Juan Antonio Valiño García ([juanval@edu.xunta.es](mailto:juanval@edu.xunta.es)). Amtega - Xunta de Galicia
