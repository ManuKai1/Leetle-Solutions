def solve(root):
  if not root:
    return []
  return [root.val] + solve(root.left) + solve(root.right)
