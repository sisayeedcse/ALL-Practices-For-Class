def DELETE(LA, N, K):
    J = K
    while J < N - 1:
        LA[J] = LA[J + 1]
        J = J + 1
    LA.pop() 
    N = N - 1
    return LA

LA = input("Enter elements separated by space: ")
LA = [int(x) for x in LA.split()]
N = len(LA)
K = int(input("Enter the position: "))

print(DELETE(LA, N, K))
