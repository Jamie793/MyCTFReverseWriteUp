import z3

solver = z3.Solver()
x = z3.Int('x')
solver.add(x > 10000000)
solver.add(x < 0x5F5E0FF)
solver.add(z3.Abs(x / 1000 % 100 - 36) == 3)
solver.add(x % 1000 % 584 == 0)

t = 1
t1 = 10000000
for i in range(3):
    solver.add(x / t % 10 == x / t1 % 10)
    t *= 10
    t1 /= 10

y = z3.RoundNearestTiesToAway()(x / 1000000)
solver.add(
    z3.Or(
        z3.And((y > ord('0'), y < ord('9'))),
        z3.And((y > ord('a'), y < ord('z'))),
        z3.And((y > ord('A'), y < ord('Z'))),
        ))


y = round(x / 10000 % 100
solver.add(
    z3.Or(
        z3.And((y > ord('0'), y < ord('9'))),
        z3.And((y > ord('a'), y < ord('z'))),
        z3.And((y > ord('A'), y < ord('Z'))),
        ))


y = x //  100 % 100 + 10
solver.add(
    z3.Or(
        z3.And((y > ord('0'), y < ord('9'))),
        z3.And((y > ord('a'), y < ord('z'))),
        z3.And((y > ord('A'), y < ord('Z'))),
        ))


# while solver.check() == z3.sat:
#   print(solver.model())
#   solver.add(x != solver.model()[x])

if solver.check() == z3.sat:
    print("Congratulations!")
    model = solver.model()
    print(model)

