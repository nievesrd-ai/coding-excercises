class Solution:
    def findMaxConsecutiveOnes(self, nums):
        array_length = len(nums)
        if array_length == 1:
            if nums[0] == 1:
                return 1
            else:
                return 0
        in_window = False
        current_window_length = 0
        max_window_length = 0
        window_delta = 0
        j = 0
        
        while j < array_length:
            current_value = nums[j]
            if current_value and not(in_window):
                in_window = True
                current_window_length = 1
            window_delta+=1
            if j + window_delta < array_length:
                next_value = nums[j+window_delta]
                if next_value and current_value:
                    if not in_window:
                        in_window = True
                    current_window_length+=1

                else:
                    if in_window:
                        if current_window_length > max_window_length:
                            max_window_length = current_window_length
                            current_window_length = 1
                        in_window = False
                    j = j + window_delta
                    window_delta = 0
            else:
                break
        if current_window_length > max_window_length:
             max_window_length = current_window_length
        return max_window_length 

finder = Solution()
a = [1, 1, 0, 1, 1, 1]
print(finder.findMaxConsecutiveOnes(a))