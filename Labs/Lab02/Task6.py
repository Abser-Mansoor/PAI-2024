def multiplication(nums) :
    ans = 1
    for num in nums :
        ans *= num
    return ans
print(multiplication([1,2,3,4,5]))
