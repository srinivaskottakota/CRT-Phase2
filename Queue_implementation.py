def enqueue(Q, ele):
    Q.append(ele)
    print(ele,"inserted into Queue")
    #print(Q)
    return Q
def dequeue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return 
    print(Q[0],"is getting deleted")
    Q.pop(0)
    #print(Q)
Q=[]
enqueue(Q, 23)
enqueue(Q, 45)
enqueue(Q, 67)
enqueue(Q, 78)

dequeue(Q)
dequeue(Q)
dequeue(Q)
dequeue(Q)
dequeue(Q)
