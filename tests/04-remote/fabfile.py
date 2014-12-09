from fabric.api import run, cd, env, settings

env.hosts = ['10.10.10.10']

def deploy():
    code_dir = '/tmp/asdf'
    with settings(warn_only=True):
        run('mkdir {}'.format(code_dir))
    with cd(code_dir):
        run('touch file')
