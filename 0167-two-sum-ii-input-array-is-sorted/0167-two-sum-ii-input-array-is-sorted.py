class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i]+numbers[j] == target:
                result.append(i+1)
                result.append(j+1)
                break
            else:
                if numbers[i]+numbers[j] > target:
                    if numbers[i] > numbers[j]:
                        i = i+1
                    else:
                        j = j-1
                else:
                    if numbers[i] < numbers[j]:
                        i = i+1
                    else:
                        j = j-1
        return result