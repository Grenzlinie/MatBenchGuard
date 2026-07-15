def invert_6x6(A):
    """Invert a 6x6 matrix using Gaussian elimination with partial pivoting."""
    n = 6
    # Augment A with identity
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        # find pivot
        pivot_row = max(range(col, n), key=lambda i: abs(aug[i][col]))
        if abs(aug[pivot_row][col]) < 1e-12:
            raise ValueError("Matrix is singular")
        # swap rows
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        # normalize pivot row
        pivot_val = aug[col][col]
        aug[col] = [v / pivot_val for v in aug[col]]
        # eliminate other rows
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [r - factor * p for r, p in zip(aug[row], aug[col])]
    # extract inverse (right half)
    inv = [row[n:] for row in aug]
    return inv
