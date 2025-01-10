def atof(s: str):
    s = s.strip()  # trim white space
    sign = -1 if s[0] == "-" else 1
    s = s[1:] if s[0] in "-+" else s
    val = 0.0
    r = s
    for c in s:
        if c == ".":
            break
        if not c.isdigit():
            break
        val = (10 * val) + (ord(c) - ord("0"))
        r = r[1:]

    r = r[1:] if len(r) > 0 and r[0] == "." else r
    power = 1.0
    for c in r:
        if not c.isdigit():
            break
        val = (10 * val) + (ord(c) - ord("0"))
        power *= 10.0

    return sign * val / power


print(atof("  -123.45 "))
print(atof("   +456.78  "))
print(atof("   789  "))
