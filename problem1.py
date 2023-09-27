class Solution:
    def defangIPaddr(self, address: str) -> str:
        return(address.replace('.', '[.]'))
        

x = Solution()
z = x.defangIPaddr("1.1.1.1.")
print(z)