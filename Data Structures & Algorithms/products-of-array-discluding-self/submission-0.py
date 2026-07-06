class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1]
        rightProducts = [1]

        product = 1
        for num in nums:
            product *= num
            leftProducts.append(product)
        leftProducts.append(1)

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            rightProducts.append(product)
        rightProducts.append(1)
        rightProducts.reverse()

        res = []
        for i in range(1, len(nums) + 1):
            res.append(leftProducts[i-1] * rightProducts[i+1])

        return res
        