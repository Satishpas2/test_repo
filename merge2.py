def f(fx):
...     print('fx =', fx, '/ id(fx) = ', id(fx))
...     fx = 10
...     print('fx =', fx, '/ id(fx) = ', id(fx))


def f(my_list=[]):
...     print(id(my_list))
...     my_list.append('###')
...     return my_list
