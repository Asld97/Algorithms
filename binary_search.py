
#list = [1,2,3,4,5]
#value = [4]
#answer = 2
from math import ceil, floor

def binary_search(list, value):
    left_index = 0
    right_index = len(list) - 1   
    

    while left_index <= right_index:
        
        medium_index = (left_index + right_index) // 2    
      
        if value > list[medium_index]:
            left_index = medium_index + 1
     
        elif value < list[medium_index]:
            right_index = medium_index - 1
   
        else:            
            return medium_index

    return None
    
        




print(binary_search([1,2,3,4,5,6,7,8], 1)) # [3] -> 4, 