from fabric.api import run, cd, env, settings, hide

env.hosts = ['10.10.10.10']

def deploy():
    code_dir = '/tmp/asdf'
    with settings(hide('everything'), warn_only=True):
        run('mkdir {}'.format(code_dir))
    with cd(code_dir):
        run('touch file')
