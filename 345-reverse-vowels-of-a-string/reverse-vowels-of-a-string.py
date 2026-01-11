class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        vowels = ['a','e','i','o','u']
        l,r = 0,n-1
        st = list(s)
        while l<r:
            if st[l].lower() not in vowels:
                l+=1
                continue
            if st[r].lower() not in vowels:
                r-=1
                continue
            st[l], st[r] = st[r],st[l]
            l+=1
            r-=1
        return "".join(st)
        