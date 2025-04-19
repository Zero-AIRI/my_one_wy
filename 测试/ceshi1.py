class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # 普通树的关键：子节点列表

# 构建树
root = TreeNode("校长")
vp1 = TreeNode("教学副校长")
vp2 = TreeNode("行政副校长")

root.children = [vp1, vp2]  # 根节点有两个子节点

# 继续添加
vp1.children = [TreeNode("数学组"), TreeNode("语文组")]  # 教学副校长下属
vp2.children = [TreeNode("财务科"), TreeNode("人事科"), TreeNode("后勤科")]  # 注意这里有三个子节点

class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # 二叉树的关键：明确区分左右
        self.right = None

# 构建二叉树
root = BinaryNode(50)  # 假设这是比赛最终冠军
root.left = BinaryNode(30)  # 半决赛A组胜者
root.right = BinaryNode(70)  # 半决赛B组胜者

# 继续构建比赛树
root.left.left = BinaryNode(20)  # 四分之一决赛
root.left.right = BinaryNode(40)
root.right.left = BinaryNode(60)
root.right.right = BinaryNode(80)


def print_tree(node, indent=""):
    print(indent + str(node.data))
    if hasattr(node, 'children'):  # 普通树
        for child in node.children:
            print_tree(child, indent + "    ")
    else:  # 二叉树
        if node.left: print_tree(node.left, indent + "    ")
        if node.right: print_tree(node.right, indent + "    ")
print("\n普通树结构：")
print_tree(root)
print("\n二叉树结构：")
print_tree(root)  # 注意：这里的root是之前二叉树示例的根节点
