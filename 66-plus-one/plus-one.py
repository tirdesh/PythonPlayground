class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j= len(digits)-1
        carry = 1
        while carry and j>=0:
            if digits[j]==9:
                digits[j]=0
                carry=1
            else:
                digits[j]+=carry
                carry=0
            j-=1
        if carry==1:
            digits.insert(0,1)
        return digits