# Ansible environment role

This is an [Ansible](http://www.ansible.com) role which manages device special files.

## Requirements

[Ansible 2.5+](http://docs.ansible.com/ansible/latest/intro_installation.html)

## Role Variables

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
    - amtega.dev
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

Tests are based on docker containers. You can setup docker engine quickly using the playbook `files/setup.yml` available in the role [amtega.docker_engine](https://galaxy.ansible.com/amtega/docker_engine).

Once you have docker, you can run the tests with the following commands:

```shell
$ cd amtega.dev/tests
$ ansible-playbook --skip-tags "role::docker_engine" main.yml
```

## License

Copyright (C) 2017 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify
it under the terms of:
GNU General Public License version 3, or (at your option) any later version;
or the European Union Public License, either Version 1.2 or – as soon
they will be approved by the European Commission ­subsequent versions of
the EUPL;

This role is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
