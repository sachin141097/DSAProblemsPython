def find_shortest_common_supersequence(s1, s2):
    s1_len, s2_len = len(s1), len(s2)
    dp = [[0] * (s2_len + 1) for _ in range(s1_len + 1)]
    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    scs = []
    i, j = s1_len, s2_len
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            scs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            scs.append(s1[i - 1])
            i -= 1
        else:
            scs.append(s2[j - 1])
            j -= 1
    # Add remaining characters from str1 or str2
    while i > 0:
        scs.append(s1[i - 1])
        i -= 1
    while j > 0:
        scs.append(s2[j - 1])
        j -= 1
    return "".join(reversed(scs))


s1 = "dynamic"
s2 = "program"
print(find_shortest_common_supersequence(s1, s2))
