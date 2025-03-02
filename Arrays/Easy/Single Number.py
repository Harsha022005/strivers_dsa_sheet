class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tot=0
        for n in nums:
            tot^=n
        return tot    
Summary:
The function singleNumber finds the unique number in an array where every other number appears twice except for one.

Explanation (Using XOR ^ Operator):
The XOR operation (^) has two key properties:
x ^ x = 0 (a number XORed with itself cancels out).
x ^ 0 = x (a number XORed with 0 remains unchanged).
The function initializes tot = 0 and XORs all elements in nums:
Since pairs cancel out (a ^ a = 0), only the unique number remains.
Time Complexity:
O(N) (where N is the number of elements in nums), as we iterate through the array once.
Space Complexity:
O(1), since only a single variable (tot) is used.
