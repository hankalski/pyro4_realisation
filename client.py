import Pyro4

uri = input("What is the Pyro uri of the greeting object? ").strip()
n = 8

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.Factor(n))
