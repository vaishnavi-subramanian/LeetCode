class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftval = max(leftmax,0)
            rightval = max(rightmax,0)
            res[0]= max( res[0], root.val+leftval +rightval)
            return root.val+max(leftval,rightval)
        dfs(root)
        return res[0]