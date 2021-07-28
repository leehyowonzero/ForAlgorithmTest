import copy

def ispossible(start, destination):
    if(start == destination[0]):
        return True
    return False

def dfs(start, leasttickets, ans ,cnt):
    global answer
    global n
    if cnt == n and answer == []:
        answer = ans[:]
        return
    
    for i in range(len(leasttickets)):
        beforticket = copy.deepcopy(leasttickets)
        if(ispossible(start, leasttickets[i])):
            chosse = beforticket[i][1]
            ans.append(chosse)
            beforticket.pop(i)
            # print(ans)
            # print(beforticket)
            dfs(chosse,beforticket,ans,cnt+1 )
            ans.pop(-1)
            
def solution(tickets):
    global answer
    answer = []
    start = "ICN"
    global n 
    n = len(tickets)
    tickets.sort(key = lambda x : x[1])
    print(tickets)
    dfs(start, tickets, ["ICN"], 0)
    return answer