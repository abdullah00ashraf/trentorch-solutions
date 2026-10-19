def replace_char_at(s: str, index: int, ch: str) -> str:
    """
    Return a new string equal to `s` with the character at
    position `index` replaced by `ch`.
    """
    if index >= len(s) or index < -len(s):
        return s

    if index < 0:
        index += len(s)

    return s[:index] + ch + s[index + 1:]


def insert_at(s: str, index: int, text: str) -> str:
    """
    Return a new string with `text` inserted before position
    `index`.
    """
    return s[:index] + text + s[index:]


def join_with_separator(parts, sep: str) -> str:
    """
    Build and return one string containing every element of
    `parts`, with `sep` between consecutive elements.
    """
    result = ""

    for i in range(len(parts)):
        if i > 0:
            result += sep
        result += parts[i]

    return result


def repeat_text(s: str, n: int) -> str:
    """
    Return `s` repeated `n` times using the * operator.
    """
    if n <= 0:
        return ""
    return s * n


def total_chars_copied(n: int, piece_length: int) -> int:
    """
    Return the total number of characters written across all
    n steps.
    """
    if n <= 0:
        return 0

    return piece_length * (n * (n + 1) // 2)
