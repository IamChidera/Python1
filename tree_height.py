def compute_tree_height(n, parents):
    # Create an adjacency list to represent the tree
    tree = [[] for _ in range(n)]
    
    # Populate the tree using the parent information
    for i in range(n):
        if parents[i] != -1:
            tree[parents[i]].append(i)
    
    # Define a recursive DFS function to calculate the height
    def dfs(node):
        if not tree[node]:
            return 1
        else:
            heights = [dfs(child) for child in tree[node]]
            return 1 + max(heights)
    
    # Find the root of the tree
    root = parents.index(-1)
    
    # Calculate the height starting from the root
    tree_height = dfs(root)
    
    return tree_height

# Input
n = int(input())
parents = list(map(int, input().split()))

# Compute and print the tree height
height = compute_tree_height(n, parents)
print(height)
