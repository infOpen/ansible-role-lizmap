# lizmap

[![CI](https://github.com/infOpen/ansible-role-lizmap/workflows/CI/badge.svg)](https://github.com/infOpen/ansible-role-lizmap/actions)
[![Mergify Status][mergify-status]][mergify]
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-lizmap/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-lizmap/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-lizmap/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-lizmap/)
[![Ansible Role](https://img.shields.io/ansible/role/24686.svg)](https://galaxy.ansible.com/infOpen/lizmap/)

Install lizmap package.

## Requirements

This role requires Ansible 2.8 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/ansible-community/molecule) to run tests.

Local and Github Actions tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Buster
- Debian Stretch
- Ubuntu Bionic
- Ubuntu Focal

and use:
- Ansible 2.8.x
- Ansible 2.9.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Repository management
lizmap_repository_cache_valid_time: 3600
lizmap_system_prerequisites: "{{ _lizmap_system_prerequisites | default([]) }}"

# Package
lizmap_app_name: 'lizmap-web-client'
lizmap_app_version: '3.1.11'
lizmap_app_package_url: "https://github.com/3liz/{{ lizmap_app_name }}/archive/{{ lizmap_app_version }}.zip"

# User and group management
lizmap_manage_group: False
lizmap_manage_user: False
lizmap_user:
  name: 'www-data'
lizmap_group:
  name: 'www-data'

# Installation
lizmap_install_method: 'zip'
lizmap_install_root_dir:
  path: '/opt/lizmap/'
  owner: "{{ lizmap_user.name }}"
  group: "{{ lizmap_group.name }}"
  mode: '0700'

# Configuration
lizmap_install_demo_repositories: True
lizmap_persistant_crypt_key: ''
lizmap_main_config:
  - option: 'wmsServerURL'
    value: 'http://127.0.0.1/cgi-bin/qgis_mapserv.fcgi'
  - option: 'onlyMaps'
    value: 0
  - option: 'defaultRepository'
    value: ''
  - option: 'defaultProject'
    value: ''
  - option: 'cacheStorageType'
    value: 'file'
  - option: 'cacheRedisHost'
    value: 'localhost'
  - option: 'cacheRedisPort'
    value: 6379
  - option: 'cacheExpiration'
    value: 0
  - option: 'proxyMethod'
    value: 'php'
  - option: 'debugMode'
    value: 0
  - option: 'cacheRootDirectory'
    value: '/tmp/'
  - option: 'allowUserAccountRequests'
    value: 'off'
lizmap_local_config:
  - section: 'modules'
    option: 'lizmap.installparam'
    value: "{{ lizmap_install_demo_repositories | ternary('demo', '') }}"
  - section: 'coordplugins'
    option: 'lizmap'
    value: 'lizmapConfig.ini.php'
  - section: 'coordplugin_auth'
    option: 'persistant_crypt_key'
    value: "{{ lizmap_persistant_crypt_key }}"
lizmap_profiles_config:
  - section: 'jdb'
    option: 'default'
    value: 'jauth'
  - section: 'jdb'
    option: 'jacl2_profile'
    value: 'jauth'
  - section: 'jdb:jauth'
    option: 'driver'
    value: 'sqlite3'
  - section: 'jdb:jauth'
    option: 'database'
    value: 'var:db/jauth.db'
  - section: 'jdb:lizlog'
    option: 'driver'
    value: 'sqlite3'
  - section: 'jdb:lizlog'
    option: 'database'
    value: 'var:db/logs.db'
  - section: 'jcache'
    option: 'default'
    value: 'myapp'
  - section: 'jcache:myapp'
    option: 'enabled'
    value: 1
  - section: 'jcache:myapp'
    option: 'driver'
    value: 'file'
  - section: 'jcache:myapp'
    option: 'ttl'
    value: 0
  - section: 'jcache:myapp'
    option: 'cache_dir'
    value: ''
  - section: 'jcache:myapp'
    option: 'file_locking'
    value: 1
  - section: 'jcache:myapp'
    option: 'directory_level'
    value: 0
  - section: 'jcache:myapp'
    option: 'directory_umask'
    value: ''
  - section: 'jcache:myapp'
    option: 'file_name_prefix'
    value: ''
  - section: 'jcache:myapp'
    option: 'cache_file_umask'
    value: ''
  - section: 'jcache:qgisprojects'
    option: 'enabled'
    value: 1
  - section: 'jcache:qgisprojects'
    option: 'driver'
    value: 'file'
  - section: 'jcache:qgisprojects'
    option: 'ttl'
    value: 0
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.lizmap }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- https://www.infopen.pro
- a.chaussier [at] infopen.pro

[mergify]: https://mergify.io
[mergify-status]: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/infOpen/ansible-role-lizmap&style=flat
