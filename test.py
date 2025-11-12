from core import Value

x = Value(2.0)
y = x**2 + 3*x
print(y.recompute_with_value(x, 3.0))
