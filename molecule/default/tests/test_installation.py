"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('xauth'),
    ('python3-simplejson'),
    ('python3-software-properties'),
    ('unzip'),
])
def test_packages(host, name):
    """
    Ensure QGIS Server packages installed
    """

    assert host.package(name).is_installed


@pytest.mark.parametrize('path', [
    ('/opt/lizmap/'),
    ('/opt/lizmap/current/lizmap/var/config'),
    ('/opt/lizmap/current/lizmap/var/log'),
])
def test_folders(host, path):
    """
    Ensure some lizmap folders exists
    """

    current_dir = host.file(path)

    assert current_dir.exists
    assert current_dir.is_directory
    assert current_dir.user == 'www-data'
    assert current_dir.group == 'www-data'


@pytest.mark.parametrize('path', [
    ('/opt/lizmap/current/lizmap/var/config/lizmapConfig.ini.php'),
    ('/opt/lizmap/current/lizmap/var/config/localconfig.ini.php'),
    ('/opt/lizmap/current/lizmap/var/config/profiles.ini.php'),
])
def test_config_files(host, path):
    """
    Ensure Lizmap main config files exists
    """

    current_file = host.file(path)

    assert current_file.exists
    assert current_file.is_file
    assert current_file.user == 'www-data'
    assert current_file.group == 'www-data'
