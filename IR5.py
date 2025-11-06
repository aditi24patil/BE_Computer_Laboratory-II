# IR-5 : Program: PageRank Algorithm Implementation

import numpy as np

# Example: 4 pages (A, B, C, D)
# If page i links to page j, then M[j][i] = 1 / (number of outgoing links from i)

M = np.array([[0,   0,   1/2, 0],
              [1/3, 0,   0,   1/2],
              [1/3, 1/2, 0,   1/2],
              [1/3, 1/2, 1/2, 0]])

# Step 2: Initialize Parameters
n = M.shape[0]                 # number of pages
d = 0.85                       # damping factor
tolerance = 0.0001             # convergence threshold
r = np.ones(n) / n             # initial PageRank (uniform distribution)

# Step 3: Iteratively Compute PageRank
while True:
    new_r = (1 - d) / n + d * M.dot(r)
    if np.linalg.norm(new_r - r, ord=1) < tolerance:
        break
    r = new_r

# Step 4: Display Results
pages = ['A', 'B', 'C', 'D']
print("Final PageRank Scores:")
for i in range(n):
    print(f"Page {pages[i]}: {r[i]:.4f}")
