import math

# Terminal node values (leaf nodes)
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Alpha-Beta recursive function
def alphabeta(depth, nodeIndex, maxPlayer, values, alpha, beta):

    # If leaf node is reached, return its value
    if depth == 3:
        return values[nodeIndex]

    # MAX player's turn
    if maxPlayer:

        best = -math.inf

        # Explore both children
        for i in range(2):

            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, val)

            # Update alpha
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                print("Pruning at MAX node")
                break

        return best

    # MIN player's turn
    else:

        best = math.inf

        # Explore both children
        for i in range(2):

            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, val)

            # Update beta
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                print("Pruning at MIN node")
                break

        return best

# Driver code
print("Leaf Node Values:", values)

result = alphabeta(
    depth=0,
    nodeIndex=0,
    maxPlayer=True,
    values=values,
    alpha=-math.inf,
    beta=math.inf
)

print("\nOptimal Value:", result)

print("\nLogic:")
print("Alpha stores the best value found by MAX.")
print("Beta stores the best value found by MIN.")
print("When alpha becomes greater than or equal to beta,")
print("remaining branches are ignored because they cannot")
print("change the final decision.")
print("This reduces the number of nodes evaluated while")
print("producing the same optimal result.")