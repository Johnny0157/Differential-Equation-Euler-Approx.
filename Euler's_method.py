def f(x,y):
    return x**2 # define the differential equation (solution is some y(x))

n_steps = int(40000000000) # number of steps used... must be a positive integer!!!!
wanted_x = 5 # x value for estimated y(x))

x = 1 # anchoring input
y = 1/3 # anchoring output

delta_x = (wanted_x - x)/n_steps

i = 1

for i in range (0,n_steps):
    y = y + delta_x*f(x,y)
    x = x + delta_x
    i += 1

y_estimate = (x,y)
print(f"y({wanted_x}) ~ {y_estimate}")
    