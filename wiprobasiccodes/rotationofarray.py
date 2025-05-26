import sys

def solve():
    # Read input
    n = int(sys.stdin.readline())
    # Read scores, only need their sign (or whether they are negative)
    scores_str = sys.stdin.readline().split()
    initial_scores = [int(s) for s in scores_str]
    k = int(sys.stdin.readline())

    # Determine which scores need to be flipped (0 means no flip, 1 means flip needed)
    flip_needed = [0] * n
    for i in range(n):
        if initial_scores[i] < 0:
            flip_needed[i] = 1

    # Determine which applicants need to be targeted (0 means don't target, 1 means target)
    # target[i] = 1 if we target applicant with 0-based index i
    target = [0] * n
    required_targets_count = 0

    # Calculate targets sequentially
    if n > 0:
        # Base case: target for index 0
        target[0] = flip_needed[0]
        required_targets_count += target[0]

        # Inductive step: target for index i depends on target[i-1] and flip_needed[i]
        for i in range(1, n):
            # We need (target[i] + target[i-1]) % 2 == flip_needed[i]
            # target[i] = (flip_needed[i] - target[i-1]) mod 2
            target[i] = (flip_needed[i] - target[i-1] + 2) % 2 # +2 ensures non-negative before mod
            required_targets_count += target[i]

    # Check if the required number of targets is within the limit K
    if required_targets_count > k:
        print("-1")
    else:
        # Collect the 1-based IDs of the targeted applicants
        result_ids = []
        for i in range(n):
            if target[i] == 1:
                result_ids.append(i + 1)

        # Print the result IDs space-separated
        # The * operator unpacks the list elements for print
        print(*(result_ids))

# Run the solver function
solve()