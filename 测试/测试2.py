class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val    
        self.left = left  
        self.right = right  

di_yi_ge_shu1 = TreeNode(1)  # 根节点                                          
di_yi_ge_shu2 = TreeNode(2)  
di_yi_ge_shu3 = TreeNode(3)
di_yi_ge_shu4 = TreeNode(4,left = None,right = None)  
di_yi_ge_shu5 = TreeNode(5,left = TreeNode(5)  ,right = TreeNode(6)  )
di_yi_ge_shu6 = TreeNode(7, left=TreeNode(8), right=TreeNode(9))


di_yi_ge_shu1.left = di_yi_ge_shu2
di_yi_ge_shu1.right = di_yi_ge_shu3
di_yi_ge_shu2.left = di_yi_ge_shu4
di_yi_ge_shu2.right = di_yi_ge_shu5
di_yi_ge_shu5.left = di_yi_ge_shu6

def qxbl_dg(root):
    if root is None:
        return []
    else:
        return [root.val] + qxbl_dg(root.left) + qxbl_dg(root.right)
    
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    #    / \
    #   7   6
    #  / \
    # 8   9


def zxbl_dg(root):
    if root is None:
        return []
    else:
        return zxbl_dg(root.left) + [root.val] + zxbl_dg(root.right)
    
print("第一个树:", qxbl_dg(di_yi_ge_shu1))
print("第一个树:", zxbl_dg(di_yi_ge_shu1))