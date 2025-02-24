# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(root):
  valid = True
  if root == None:
    return (True, None, None)
  resultLeft = traverse(root.left)
  valid = valid and resultLeft[0]
  resultRight = traverse(root.right)
  valid = valid and resultRight[0]
  maxLeft = root.val
  minRight = root.val
  if root.left != None:
    valid = valid and resultLeft[1] < root.val
    maxLeft = max(resultLeft[1], maxLeft)
    minRight = min(resultLeft[2], minRight)
  if root.right != None:
    valid = valid and resultRight[2] > root.val
    minRight = min(resultRight[2], minRight)
    maxLeft = max(resultRight[1], maxLeft)
  res = (valid, maxLeft, minRight)
  return res

def solve(root):
  return traverse(root)[0]