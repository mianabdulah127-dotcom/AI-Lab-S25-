count = 0
def alpha_beta(tree, start, end, is_max, alpha, beta):
    global count
    if start == end:
        count += 1
        return tree[start]
    mid = (start + end) // 2
    if is_max:
        left = alpha_beta(tree, start, mid, False, alpha, beta)
        alpha = max(alpha, left)
        if alpha >= beta:
            return left
        right = alpha_beta(tree, mid + 1, end, False, alpha, beta)
        return max(left, right)
    else:
        left = alpha_beta(tree, start, mid, True, alpha, beta)
        beta = min(beta, left)
        if alpha >= beta:
            return left
        right = alpha_beta(tree, mid + 1, end, True, alpha, beta)
        return min(left, right)
tree = [-1, 0, 2, 1, 9, 6, 5, 3]
result = alpha_beta(tree, 0, 7, True, -1000, 1000)
print("Final Minimax Value:", result)
print("Leaf Evaluations:", count)
