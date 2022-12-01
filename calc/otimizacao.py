from sympy import symbols, pi, N, diff, solve, Eq

D = symbols('D')
h = symbols('h')

v = (pi * D**2) + 2 * pi * D + 10
dv = diff(v)
pc = solve(Eq(dv, 0), D)
vmin = v.subs(D, -1)


def minimo(volume):
    t = N(vmin) * h
    altura = solve(Eq(t, volume), h)

    return altura[0], N(vmin)
