class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        product = 1
        for num in nums:
            product *= num
            prefix.append(product)
        prefix.append(1)

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            postfix.append(product)
        postfix.append(1)
        postfix.reverse()

        res = []
        for i in range(1, len(nums) + 1):
            res.append(prefix[i-1] * postfix[i+1])

        return res
        