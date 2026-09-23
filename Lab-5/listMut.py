"""
Write a function remove_last(lst) that removes the last element of a list. 
Call this function with a list and check whether the original list changes outside the function. 
"""
def remove_last(lst):
  
    if lst:
        return lst.pop()
    return None


my_list = [10, 20, 30, 40]

print("Before function call:", my_list)

removed_item = remove_last(my_list)

print("Returned item:", removed_item)
print("After function call:", my_list)
