struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        this->sumNumbers(root, 0);
    }

    int sumNumbers(TreeNode *root, int prefix){
        if (!root) return 0;
        if (!root->left) && (!root->right){
            return prefix * 10 + root->val;
        }
        int ret = 0, my_prefix = prefix * 10 + root->val;
        if (root->left) ret += this->sumNumbers(root->left, my_prefix);
        if (root->right) ret += this->sumNumbers(root->right, my_prefix);
        return ret
    }
};