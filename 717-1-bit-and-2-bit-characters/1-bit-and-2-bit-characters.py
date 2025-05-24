class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #Nikhil1
        
        n = len(bits)

        i=0
        while (i<n):
            if bits[i]==1:
                i=i+2
            elif bits[i]==0:
                i=i+1
                if i==n:
                    return True
        return False