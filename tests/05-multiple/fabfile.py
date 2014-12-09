from fabric.api import run, env, roles, put, execute

env.user = 'vagrant'
env.roledefs = {
    'web': ['10.10.10.11', '10.10.10.12', '10.10.10.13'],
    'db': ['10.10.10.13', '10.10.10.14'],
}

env.key_filename = '~/.vagrant.d/insecure_private_key'

@roles('web')
def install_app():
    put('app', '/tmp')

@roles('web')
def restart_app():
    run('python /tmp/app/main.py')

@roles('web')
def deploy_app():
    install_app()
    restart_app()

@roles('db')
def migrate_db():
    run('echo migrate db')

def full_deploy():
    execute(migrate_db)
    execute(deploy_app)
