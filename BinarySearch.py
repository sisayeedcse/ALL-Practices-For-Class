def BINARY(DATA,N,ITEM,LOW,HIGH):
    
    MID = (LOW + HIGH)//2

    while LOW <= HIGH:
        if DATA[MID] == ITEM:
            return MID
        elif DATA[MID] < ITEM:
            LOW = MID + 1
        else:
            HIGH = MID - 1
        MID = (LOW + HIGH)//2
    return -1


DATA = [1,2,3,4,5,6,7,8,9,10,12,15,18,19,20,35,50,78,98,102]
ITEM = 12
N = len(DATA)
LOW = 0
HIGH = N + 1
RESULT = BINARY(DATA,N,ITEM,LOW,HIGH)
if RESULT == -1:
    print("ITEM NOT FOUND")
else:
    print(f"ITEM IS FOUND AT POSITION- ",RESULT)