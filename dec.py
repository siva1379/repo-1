def outer(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner
@outer
def main():
    return "hello world"
print(main())

