from .helpers import (
    juju,
    JUJU_VERSION,
)


def add_storage(unit, name, pool=None, count=None, size=None):
    """Add storage to a unit.

    :param unit: Unit on which to add storage, e.g. "wordpress/0"
    :param name: Storage name
    :param pool: Storage pool name
    :param count: Storage instance count
    :param size: Storage instance minimum size

    """
    if '/' not in unit:
        raise ValueError('%s is not a unit' % unit)

    if JUJU_VERSION.major == 1:
        cmd = ['storage', 'add']
    else:
        cmd = ['add-storage']

    constraints = ','.join([
        str(constraint or '') for constraint in (pool, count, size)])
    cmd.append(unit)
    cmd.append('{}={}'.format(name, constraints))

    return juju(cmd)
