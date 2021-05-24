from timeit import Timer
from graph_tsp import graph_tsp
def runCode():
    var = str(input("Enter filename (with no extension): "))
    T = graph_tsp(var)
t1 = Timer("""runCode()""", """from __main__ import runCode""")
print("Time for Completion (seconds): " '{0:.1f}'.format(t1.timeit(1)))
