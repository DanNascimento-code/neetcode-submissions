class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}   #empty dictionary

        for i, n in enumerate(nums):  #i equals list index, n equals this index value
            indices[n] = i    # indices key == list value, indices value == list index

        for i, n in enumerate(nums):   #i equals list index, n equals this index value
            diff = target - n          #diff == target - n list index value
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []      
        


#example: nums = [2, 3, 4, 5, 6], target = 9
# first loop:
#   indices = {2: 0}
#   indices = {2: 0, 3: 1}
#   indices = {2: 0, 3: 1, 4: 2} 
#   indices = {2: 0, 3: 1, 4: 2, 5: 3}     
#   indices = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4}        

# second loop:
#   Iteration 1 (i = 0, n = 2):
#   diff = 9 - 2   result = 7
#   if 7 is contained in indices dict and indices[7] != 0:
#       --> False (7 is not in the dictionary)
#   
#   Iteration 2 (i = 1, n = 3):
#   diff = 9 - 3   result = 6
#   if 6 is contained in indices dict and indices[6] != 1:
#       --> True (6 is in the dictionary at index 4, and 4 != 1)
#       --> Match found! Returns [1, 4]
