import json


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class CreateBinaryTree:
    def __init__(self, root):
        self.root = BinaryTree(root)


sum = [0]
max_level = [-(2 ** 32)]


def BinaryTreeNodeDepthSum(root, level):
    if root is None:
        return

    if level > max_level[0]:
        sum[0] = root.data
        max_level[0] = level

    elif level == max_level[0]:
        sum[0] = sum[0] + root.data

    BinaryTreeNodeDepthSum(root.left, level + 1)
    BinaryTreeNodeDepthSum(root.right, level + 1)
    pass


if __name__ == '__main__':
    const = '''
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": null, "value": 1},
      {"id": "2", "left": null, "right": null, "value": 2}
    ],
    "root": "1"
  }
}'''
    root = json.loads(const)
    nodelist = []
    binaryTree = CreateBinaryTree(int(root['tree']['nodes'][0]['value']))
    if root['tree']['nodes'][0]['left']:
        binaryTree.root.left = BinaryTree(int(root['tree']['nodes'][0]['left']))
        nodelist.append((binaryTree.root.left, int(root['tree']['nodes'][0]['left'])))
    if root['tree']['nodes'][0]['right']:
        binaryTree.root.right = BinaryTree(int(root['tree']['nodes'][0]['right']))
        nodelist.append((binaryTree.root.right, int(root['tree']['nodes'][0]['right'])))
    for node in root['tree']['nodes'][1:]:
        for n in nodelist:
            if int(node['value']) == n[1]:
                if node['left']:
                    n[0].left = BinaryTree(int(node['left']))
                    nodelist.append((n[0].left, int(node['left'])))
                if node['right']:
                    n[0].right = BinaryTree(int(node['right']))
                    nodelist.append((n[0].right, int(node['right'])))

    BinaryTreeNodeDepthSum(binaryTree.root, 0)
    print(sum[0])
