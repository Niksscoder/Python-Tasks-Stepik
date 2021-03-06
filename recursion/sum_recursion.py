# sum recursion
def list_sum_recursive(list_):
    if len(list_)==1:
        return list_[0]
    else:
        return list_[0]+list_sum_recursive(list_[1:])

l = list(map(int,input().split()))
