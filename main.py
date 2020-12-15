import json


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class CreateBinaryTree:
    def __init__(self, root):
        self.root = BinaryTree(root)

        
def BinaryTreeNodeDepthSum(root):
    final = [0]
    helper(root, 0, final)
    return final[0]


def helper(node, d, final):
    if not node:
        return
    final[0] += d
    helper(node.left, d + 1, final)
    helper(node.right, d + 1, final)



if __name__ == '__main__':
    const = '''
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": "6", "right": "7", "value": 3},
      {"id": "4", "left": "8", "right": "9", "value": 4},
      {"id": "5", "left": null, "right": null, "value": 5},
      {"id": "6", "left": null, "right": null, "value": 6},
      {"id": "7", "left": null, "right": null, "value": 7},
      {"id": "8", "left": null, "right": null, "value": 8},
      {"id": "9", "left": null, "right": null, "value": 9}
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

    print(BinaryTreeNodeDepthSum(binaryTree.root))
