class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val    
        self.left = left  
        self.right = right  

di_yi_ge_shu1 = TreeNode(1)  # 根节点                                          


simple_tree = TreeNode(777, TreeNode(888), TreeNode(999))

# 测试用例1：简单树
#     777
#    /   \
#  888   999

# 递归前序遍历
def qxbl_dg(root):
    if root is None:
        return []
    else:
        return [root.val] + qxbl_dg(root.left) + qxbl_dg(root.right)

# 非递归前序遍历
def qxbl_fdg(root):
    if root is None:
        return []
    
    stack = [root]  # 初始化栈
    result = []     # 存储遍历结果
    
    while stack:
        node = stack.pop()
        result.append(node.val)  # 访问当前节点
        
        # 先压入右子节点，再压入左子节点（保证左子节点先出栈）
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    
    return result

# 测试用例1：简单树
#     777
#    /   \
#  888   999
simple_tree = TreeNode(777, TreeNode(888), TreeNode(999))

node1 = TreeNode(1)  # 根节点
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node6
node5.right = node7
node6.left = node8
node3.right = node9



# 测试用例2：复杂树
#        1                                 
#      /   \
#     2     3
#    / \     \
#   4   5     9
#      / \
#     6   7
#    /
#   8

def qxbl_dg(root):
    if root is None:
        return []
    else:
        return [root.val] + qxbl_dg(root.left) + qxbl_dg(root.right)



# 空树测试
empty_tree = None


print("第一个树:", qxbl_dg(node1))



# 测试输出
print("递归前序遍历:")
print("简单树:", qxbl_dg(simple_tree))
print("复杂树:", qxbl_dg(node1))
print("空树:", qxbl_dg(empty_tree))

print("\n非递归前序遍历:")
print("简单树:", qxbl_fdg(simple_tree))
print("复杂树:", qxbl_fdg(node1))
print("空树:", qxbl_fdg(empty_tree))

# simple_tree = TreeNode(777, TreeNode(888), TreeNode(999))

def copy_tree(root):    # 复制树的函数
    if root is None:
        return None
    new_node = TreeNode(root.val)              # 创建新节点 调用构造函数 值为原节点的值
    new_node.left = copy_tree(root.left)       # 
    new_node.right = copy_tree(root.right)     # 递归复制右子树
    return new_node                            # 返回新节点

copied_root = copy_tree(simple_tree)   # 进行复制

print("原树:", qxbl_dg(simple_tree))          
print("复制树:", qxbl_dg(copied_root))


def tree_depth(root):
    if root is None:
        return 0
    left_depth = tree_depth(root.left)    # 计算左子树深度
    right_depth = tree_depth(root.right)  # 计算右子树深度
    return 1 + max(left_depth, right_depth)  # 当前深度 = 1 + 左右子树的最大深度


print("树的深度:", tree_depth(node1))  


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

print("节点总数:", count_nodes(node1))  


class ThreadedNode:
    def __init__(self, val):
        self.val = val
        self.left = None    # 左子树 或 前驱线索
        self.right = None   # 右子树 或 后继线索
        self.left_thread = False  # True表示left是线索
        self.right_thread = False # True表示right是线索

def inorder_thread(root):
    if not root:
        return None
    
    # 初始化虚拟头节点
    dummy = ThreadedNode(-1)
    dummy.left_thread = True
    dummy.right_thread = False
    dummy.right = dummy  # 初始时，dummy的后继指向自己
    
    prev = dummy  # 前驱节点初始为dummy
    
    # 中序遍历（栈实现）
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        
        # 如果当前节点的左子树为空，设置前驱线索
        if not current.left:
            current.left = prev
            current.left_thread = True
        
        # 如果前驱节点的右子树为空，设置后继线索
        if not prev.right:
            prev.right = current
            prev.right_thread = True
        
        prev = current
        current = current.right
    
    # 最后处理prev（最后一个节点）的后继
    prev.right = dummy
    prev.right_thread = True
    
    return dummy  # 返回虚拟头节点

