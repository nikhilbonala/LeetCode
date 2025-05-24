class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count2 = bin(num2).count('1')  # Number of 1s needed
        result = 0
    
        # Step 1: Set bits in positions where num1 has 1s
        for i in reversed(range(32)):
            if num1 & (1 << i):
                result |= (1 << i)
                count2 -= 1
                if count2 == 0:
                    break

        # Step 2: If more 1s needed, fill from least significant bits
        if count2 > 0:
            for i in range(32):
                if not (result & (1 << i)):
                    result |= (1 << i)
                    count2 -= 1
                    if count2 == 0:
                        break

        return result