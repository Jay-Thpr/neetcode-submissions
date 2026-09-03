'''
product of all other elements = product of left * product of right

can do 2 passes collecting prefix multiple: 
    - left -> right gets all of the products of left
    - right -> left gets all the products of right

let's say we have:
[1, 2, 3]

then left -> right:
[1, 1, 2]
right -> left:
[6,3,1]

so final list is:
[1, 3, 2]
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ltr = [1] * len(nums)
        rtl = [1] * len(nums)

        for i in range(1, len(nums)):
            ltr[i] = ltr[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rtl[i] = rtl[i + 1] * nums[i + 1]
        
        res = []

        for i in range(len(nums)):
            res.append(ltr[i] * rtl[i])
        
        return res

        