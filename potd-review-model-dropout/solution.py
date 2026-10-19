import numpy as np

def inverted_dropout(x: np.ndarray, m: np.ndarray, p_keep: float) -> np.ndarray:
    """
    Inverted dropout, mask given directly.

    x: shape (n,), activations.
    m: shape (n,), 0/1 mask (given, not generated).
    p_keep: the keep probability used to generate m.

    Return (x * m) / p_keep.
    """
    return (x * m) / p_keep
