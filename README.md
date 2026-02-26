[![tests](https://github.com/boutetnico/ansible-role-elastalert2/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-elastalert2/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.elastalert2-blue.svg)](https://galaxy.ansible.com/boutetnico/elastalert2)

ansible-role-elastalert2
========================

This role installs and configures [ElastAlert2](https://github.com/jertel/elastalert2).

Requirements
------------

Ansible 2.15 or newer.

Supported Platforms
-------------------

- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Debian - 13 (Trixie)](https://wiki.debian.org/DebianTrixie)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                           | Required | Default                  | Choices | Comments                     |
|------------------------------------|----------|--------------------------|---------|------------------------------|
| elastalert2_version                | true     | `""`                     | string  | Empty for latest.            |
| elastalert2_dependencies           | true     |                          | list    | See `defaults/main.yml`.     |
| elastalert2_log_level              | true     | `warning`                | string  | `warning`, `info`, `debug`.  |
| elastalert2_config_dir             | true     | `/etc/elastalert2`       | string  |                              |
| elastalert2_rules_dir              | true     | `/etc/elastalert2/rules` | string  |                              |
| elastalert2_user                   | true     | `elastalert`             | string  |                              |
| elastalert2_group                  | true     | `elastalert`             | string  |                              |
| elastalert2_elasticsearch_scheme   | true     | `http`                   | string  | `http` or `https`.           |
| elastalert2_elasticsearch_host     | true     | `localhost`              | string  |                              |
| elastalert2_elasticsearch_port     | true     | `9200`                   | int     |                              |
| elastalert2_elasticsearch_username | true     | `""`                     | string  |                              |
| elastalert2_elasticsearch_password | true     | `""`                     | string  |                              |
| elastalert2_config                 | true     |                          | dict    | See `defaults/main.yml`.     |
| elastalert2_rules                  | true     | `[]`                     | list    |                              |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: boutetnico.elastalert2
          elastalert2_elasticsearch_host: localhost
          elastalert2_elasticsearch_port: 9200
          elastalert2_rules:
            - name: Test rule
              type: any
              index: "test-*"
              filter:
                - query:
                    query_string:
                      query: "level:error"
              alert:
                - debug

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
