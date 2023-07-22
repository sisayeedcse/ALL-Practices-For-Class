
def INSERT(LA,N,ITEM,K):
    LA.append(None)
    J= N
    while J >= K:
        LA[J]  = LA[J-1]
        J = J-1

    LA[K] = ITEM
    N = N+1
    return LA

LA = input("Enter a list of numbers, separated by spaces: ")
LA = [int(x) for x in LA.split()]  
N = len(LA)
ITEM = int(input("Enter the Item to insert- "))
K = int(input("Enter the Position- "))

print(INSERT(LA,N,ITEM,K))
