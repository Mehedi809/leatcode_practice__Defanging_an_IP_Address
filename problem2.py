class Solution:
    def finalValueAfterOperations(self, operations):
        for i in operations:
            x = 0
            if i == '--x' or i == 'x--':
                x-=1
                print(x)
            else:
                x+=1
                print(x)

c = Solution()
d = c.finalValueAfterOperations(["--X","X++","X++"])

