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
        res = ""
        if root == None:
            return res
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node !=None:
                res += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
            else:
                res += "None,"
        return res[:-1] #to avoid last comma
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data =="":
            return []
        nodes = str.split(data,",")
        q = deque()
        root = TreeNode(nodes[0])
        q.append(root)
        i=1
        while q:
            n = q.popleft()
            if nodes[i]!="None":
                n.left = TreeNode(nodes[i])
                q.append(n.left)
            i+=1
            if nodes[i]!="None":
                n.right = TreeNode(nodes[i])
                q.append(n.right)
            i+=1
        return root
            
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))