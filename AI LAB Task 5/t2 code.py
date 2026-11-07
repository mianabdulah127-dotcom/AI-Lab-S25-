
count = 0
def minimax(tree, start, end, is_max):
    global count
    if start == end:
        count = count + 1
        return tree[start]
    mid = (start + end) // 2
    left = minimax(tree, start, mid, not is_max)
    right = minimax(tree, mid + 1, end, not is_max)
    if is_max:
        return max(left, right)
    else:
        return min(left, right)
tree = [3, 5, 6, 9, 1, 2, 0, -1]
result = minimax(tree, 0, 7, True)
print("Minimax Result:", result)
print("Leaf Evaluations:", count)
count = 0
def alpha_beta(tree, start, end, is_max, alpha, beta):
    global count
    if start == end:
        count = count + 1
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
tree = [3, 5, 6, 9, 1, 2, 0, -1]
result = alpha_beta(tree, 0, 7, True, -1000, 1000)
print("Alpha-Beta Result:", result)
print("Leaf Evaluations:", count)