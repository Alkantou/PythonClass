def get_idx(idx):
    res = 0
    for ele in idx:
        res = (res << 1) | ele

    return res


def bfs_traverse(top):
    acc = []
    
    acc.append(top.value)
    
    
    i = 1
    current = []
    
    if top.left is not None:
        current.append((top.left,[0]))
        
    if top.left is not None:
        current.append((top.right,[1]))
    
    while len(current)>0:
        new_ = [None for _ in range(2**i)]
        for c,idx in current:
            if c:
                new_[get_idx(idx)] = c.value
        acc.extend(new_)
        
        new_current=[]
        for c,idx in current:
            if c:
                if c.left is not None:
                    cop = idx.copy()
                    cop.append(0)
                    new_current.append((c.left,cop))
                if c.right is not None:
                    cop = idx.copy()
                    cop.append(1)
                    new_current.append((c.right,cop))
            
        current = new_current
        i += 1
    
    return acc
