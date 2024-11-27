class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        #hashmap where key is id of student and value is a priority queue of length 5
        studentsMap = {}
        for i in items:
            if i[0] not in studentsMap.keys():
                studentsMap[i[0]] = [i[1]]
                heapq.heapify(studentsMap[i[0]])
            else:
                #do the priority queue operations
                if  len(studentsMap[i[0]])==5:
                    if i[1] > studentsMap[i[0]][0]:
                        heapq.heappop(studentsMap[i[0]])
                        heapq.heappush(studentsMap[i[0]],i[1])
                else:
                    heapq.heappush(studentsMap[i[0]],i[1])
        ans = []
        for s in studentsMap.keys():
            average = sum(studentsMap[s])//5
            ans.append([s,average])
        return sorted(ans)
        
                
                    