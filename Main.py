from numpy import asarray
from numpy import arange
from numpy.random import rand
from matplotlib import pyplot
def objective(x):
    return x**2.0
def derivative (x):
    return x*2.0
def gradientdescented(objective,derivative,bonds,n,stepsize):
    solutions,score=list(),list()
    solution=bonds[:,0]+rand(len(bonds))*(bonds[:,1]-bonds[:,0])
    for i in range (n):
        gradient=derivative(solution)
        solution=solution-stepsize*gradient
        solutionsevalvulation=objective(solution)
        solutions.append(solution)
        score.append(solutionsevalvulation)
        print(f"{i}={solution},{solutionsevalvulation}")
    return[solutions,score]
bonds=asarray([[-1.0,1.0]])
n=30
stepsize=0.1
solutions,scores=gradientdescented(objective,derivative,bonds,n,stepsize)
input=arange(bonds[0,0],bonds[0,1]+0.1,0.1)
result=objective(input)
pyplot.plot(input,result)
pyplot.plot(solutions,scores,".-",color="red")
pyplot.show()