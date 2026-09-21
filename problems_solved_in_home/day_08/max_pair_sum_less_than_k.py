class Solution:
    def maxSum(self, arr, k):
        arr.sort()
        left = 0
        right = len(arr) - 1
        max_sum = -1
        max_diff = -1
        answer = (-1, -1)
        while left < right:
            current_sum = arr[left] + arr[right]
            current_diff = arr[right] - arr[left]
            if current_sum < k:
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_diff = current_diff
                    answer = (arr[left], arr[right])
                elif current_sum == max_sum:
                    if current_diff > max_diff:
                        max_diff = current_diff
                        answer = (arr[left], arr[right])
                left += 1
            else:
                right -= 1
        return answer