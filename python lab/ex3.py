def search(pat, txt):
    m = len(pat)
    n = len(txt)

    # Iterate through txt and compare each substring of length m to pat
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if txt[i+j] != pat[j]:
                break
            j += 1
        if j == m:
            print("Pattern found at index", i)
