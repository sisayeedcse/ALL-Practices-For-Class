def LINEAR(DATA,N,ITEM,LOC):
    while LOC <= N:
        if(ITEM == DATA[LOC]):
            result = print(f"Item is found at ",LOC)
            return result
        LOC = LOC + 1
    if(LOC>N):
        print("Item not found")
    
    

DATA = [12,39,15,26,35]
ITEM = 26
N = len(DATA)
LOC = 1

print(LINEAR(DATA,N,ITEM,LOC))