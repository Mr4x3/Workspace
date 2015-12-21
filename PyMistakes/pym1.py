def foo(bar=[]):
    bar.append('\x55\x32\x34')
    return bar

print(foo())
print(foo())
print(foo())
print(foo()*3)
print(['baz']*3)
