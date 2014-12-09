from fabric.api import run, env, roles

env.user = 'vagrant'
env.roledefs = {
    'web': ['10.10.10.11', '10.10.10.12', '10.10.10.13'],
    'db': ['10.10.10.13', '10.10.10.14'],
}

env.key_filename = '~/.vagrant.d/insecure_private_key'

@roles('web', 'db')
def deploy():
    run('ls -la')
