from ortools.linear_solver import pywraplp

# GLOP is only for LP problems change to CBC which is for MILP
solver = pywraplp.Solver.CreateSolver('MILP','CBC')
# we can also use Gurobi, Cplex,

x = solver.IntVar(0,10,'x')
y = solver.NumVar(0,10,'y')

solver.Add(-x+2*y<=7)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

solver.Maximize(x+y)

results = solver.Solve()

if results==pywraplp.Solver.OPTIMAL: print('Optimal Found')

print('x:', x.solution_value())
print('y:', y.solution_value())

# Solution with CBC is x=4.0, y=5.5
