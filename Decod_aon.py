def aon_decode(stri):
    if len(stri) < 2 or stri.isalpha():
        return "empty"
    else:
        s = [each for each in stri]
        result = []
        i = 1
        string_result = ""
        while i < len(s) - 1:
            if (s[i] == s[i - 1] and s[i] == s[i + 1]) or (s[i] != s[i - 1] and s[i] != s[i + 1]) or (
                    s[i] != s[i - 1] and s[i] == s[i + 1]):
                i += 1
            else:
                result.append(s[i])
                i += 1
        if result[0] == "#":
            result.remove(result[0])
        if s[len(s) - 1] == s[len(s) - 2]:
            result.append(s[len(s) - 1])
        decoded = [each for each in result]
        for i in range(len(result)):
            if result[i] == "#":
                decoded.insert(i, result[i - 1])
                decoded.remove("#")
        for i in range(len(decoded)):
            string_result += decoded[i]
        return string_result

if __name__ == '__main__':
    print aon_decode("##332411666614327766#####5665666655###66655")
    print aon_decode("11223322444##44##66")
    print aon_decode("1122332222777#555997")
    print aon_decode("")
    print aon_decode("##112")
    print aon_decode("1")
    print aon_decode("aaa")
    print aon_decode("#11222")
else:
    print "YABABABAA"