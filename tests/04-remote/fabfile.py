from fabric.api import run, cd

def deploy():
    code_dir = '/tmp/asdf'
    run('mkdir {} && true'.format(code_dir))
    with cd(code_dir):
        run('touch file')
