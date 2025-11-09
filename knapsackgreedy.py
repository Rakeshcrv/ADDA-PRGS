class item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
def kns(w,arr):
    arr.sort(key=lambda x:(x.profit/x.weight),reverse=True)
    finalvalue=0.0
    for item in arr:
        if item.weight<=w:
            w-=item.weight
            finalvalue+=item.profit
        else:
            finalvalue+=item.profit*w/item.weight
            break
    return finalvalue
if __name__=='__main__':
    w=50
    arr=[item(60,10),item(100,20),item(120,30)]
    max_val=(kns(w,arr))
    print(max_val)