def ffxiv_lottery(map):
    def expectation_of_sel(in_sel, out_sel):
        remains = []
        if len(in_sel) + len(out_sel) != 4:
            raise ValueError("length not match")
        for i in range(1, 10):
            if i not in in_sel:
                if i not in out_sel:
                    remains.append(i)
        def profit(x):
            result = [10000, 36, 720, 360, 80, 252, 108, 72, 54, 180, 72, 180, 119, 36, 306, 1080, 144, 1800, 3600]
            return (result[x - 6])
    
        case=[]
        if len(in_sel) == 3:
            case.append(profit(sum(in_sel)))
        elif len(in_sel) == 2:
            for x in remains:
                tgt = in_sel.copy()
                tgt.append(x)
                case.append(profit(sum(tgt)))
        elif len(in_sel) == 1:
            for x in remains:
                for y in remains:
                    if y != x:
                        tgt = in_sel.copy()
                        tgt.append(x)
                        tgt.append(y)
                        case.append(profit(sum(tgt)))
        elif len(in_sel) == 0:
            for x in remains:
                for y in remains:
                    for z in remains:
                        if y != x and x!=z and y!=z:
                            tgt = in_sel.copy()
                            tgt.append(x)
                            tgt.append(y)
                            tgt.append(z)
                            case.append(profit(sum(tgt)))
        expectation = 0
        for x in case:
            expectation += x / len(case)
        return expectation

    solution = ['row1', 'row2', 'row3', 'col1', 'col2', 'col3', 'diag1', 'diag2']
    all_sel = []
    for row in map:
        for x in row:
            if x != 0:
                all_sel.append(x)
    for x in solution:
        in_sel = []
        out_sel = []
        if x == 'row1':
            tmp = [map[0][0], map[0][1], map[0][2]]
        elif x == 'row2':
            tmp = [map[1][0], map[1][1], map[1][2]]
        elif x == 'row3':
            tmp = [map[2][0], map[2][1], map[2][2]]
        elif x == 'col1':
            tmp = [map[0][0], map[1][0], map[2][0]]
        elif x == 'col2':
            tmp = [map[0][1], map[1][1], map[2][1]]
        elif x == 'col3':
            tmp = [map[0][2], map[1][2], map[2][2]]
        elif x == 'diag1':
            tmp = [map[0][0], map[1][1], map[2][2]]
        elif x == 'diag2':
            tmp = [map[0][2], map[1][1], map[2][0]]
        for i in tmp:
            if i in all_sel:
                in_sel.append(i)
        for i in all_sel:
            if i not in in_sel:
                out_sel.append(i)
        print(x,":%.2f"%expectation_of_sel(in_sel,out_sel))
        
map=[[0, 0, 0],
     [7, 2, 5],
     [6, 0, 0]]
ffxiv_lottery(map)
