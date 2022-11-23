# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] #Intialize result as an empty array
        hashmap= defaultdict(list) #Initialize hashmap as a defaultdict list
        q = deque() #Initialize q using deque
        q.append((root,0)) #Append root and 0 to the q

        while q: #Continue until q is true
            size=len(q) #Size is length of the q
            level=[] #Initialize level as an empty array
            for _ in range(size): #Continue till the size
                node,v = q.popleft()    #Initialize node and v to the last element popped out from the q
                hashmap[v].append(node.val) #Append the node.val to the hashmap[v]
                if node.left: #If there is any left child for the node
                    level.append((node.left,v-1)) #Append that node.left and v-1 to the level
                if node.right: #If there is any right child for that node
                    level.append((node.right,v+1))  #Append that node.left and v+1 to the level
            level.sort(key = lambda x: (x[1], x[0].val)) #Sorting the level with the node's value
            q = deque(level) #Assign q using deque with level
        hashmap = OrderedDict(sorted(hashmap.items())) #Change hashmap as Ordereddict of all the hashmaps' items sorted
        for k,v in hashmap.items(): #For k and v in hashmap.items
            result.append(v) #Append v to the result

        return result #Return result