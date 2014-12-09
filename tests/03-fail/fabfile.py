from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
    with settings(warn_only=True):
        result = local('false')
    if result.failed and not confirm('Failed. Continue anyway?'):
        abort('Aborting')
