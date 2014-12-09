from fabric.api import local

def ls():
    local('ls -la')

def tree():
    local('tree ..')

def prepare():
    ls()
    tree()
