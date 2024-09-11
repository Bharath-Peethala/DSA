class Solution(object):
    # naive solution
    def minBitFlips(self, start, goal):
        startBin = bin(start).replace("0b","")
        goalBin = bin(goal).replace("0b","")
        diffLen = abs(len(startBin)-len(goalBin))
        addZero = ""
        for _ in range(diffLen):
            addZero+="0"
        
        if len(startBin) > len(goalBin):
            goalBin = addZero+goalBin
        else:
            startBin = addZero+startBin

        count = 0
        for i in range(len(startBin)):
            if startBin[i]!=goalBin[i]:
                count+=1
        return count
    # xor solution
    def xorSol(self,start,goal):
        return bin(start^goal).count("1")