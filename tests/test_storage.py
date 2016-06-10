import unittest

from mock import patch

from amulet import storage


class AddStorageTest(unittest.TestCase):
    def test_bad_unit(self):
        with self.assertRaises(ValueError):
            storage.add_storage('foo', 'mystorage')

    @patch('amulet.storage.juju')
    @patch('amulet.storage.JUJU_VERSION')
    def test_juju_1(self, version, juju):
        version.major = 1
        storage.add_storage(
            'unit/0',
            'mystorage',
            pool='ebs',
            count=1,
            size=1024,
        )
        juju.assert_called_once_with([
            'storage', 'add', 'unit/0', 'mystorage=ebs,1,1024'])

    @patch('amulet.storage.juju')
    @patch('amulet.storage.JUJU_VERSION')
    def test_juju_2(self, version, juju):
        version.major = 2
        storage.add_storage(
            'unit/0',
            'mystorage',
            pool='ebs',
            count=1,
            size=1024,
        )
        juju.assert_called_once_with([
            'add-storage', 'unit/0', 'mystorage=ebs,1,1024'])
