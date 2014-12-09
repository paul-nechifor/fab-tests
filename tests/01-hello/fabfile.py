def hello(name='world', times=1):
    for i in xrange(int(times)):
        print 'Hello {}!'.format(name)
