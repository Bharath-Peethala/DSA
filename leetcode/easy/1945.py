def getLucky(s, k):
        convertedStr = ""
        luckNumber = 0
        for i in s:
            convertedStr += str(ord(i)-96)
        while(k):
            for i in str(convertedStr):
                luckNumber += int(i)
            convertedStr = luckNumber
            luckNumber = 0
            k = k-1
        return convertedStr

s = "bharath"
k = 7
print(getLucky(s,k))
