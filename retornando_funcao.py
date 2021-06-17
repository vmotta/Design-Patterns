def pai(num):

    def filho1():
        print('oi sou filho 1')

    def filho2():
        print('oi sou filho 2')

    try:
        assert num == 20
        return filho1
    except AssertionError:
        return filho2
f1 = pai(10)
f2 = pai(20)

f1()
f2()