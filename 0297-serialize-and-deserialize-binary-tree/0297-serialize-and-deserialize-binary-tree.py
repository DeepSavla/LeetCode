# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        res = ""
        q = deque()
        q.append(root)
        while len(q)>0:
            s = q.popleft()
            if s!=None:
                res = res + str(s.val) + ","
                q.append(s.left)
                q.append(s.right)
            else:
                res = res +  "None,"
        # j=len(res)-1
        # while res[j]==None:
        #     res.pop()
        #     j=j-1
        
        return res[:len(res)-1]
        
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []
        data = data.split(",")
        q = deque()
        i=0
        root = TreeNode(data[0])
        q.append(root)
        while i<len(data)-2:
            s = q.popleft()
            i+=1
            if data[i] !="None":
                s.left = TreeNode(data[i])
                q.append(s.left)
            i+=1
            if data[i] !="None":
                s.right = TreeNode(data[i])
                q.append(s.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))