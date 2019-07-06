def merge_sorted_lists(nums1, nums2):
  nums1_Index = 0
  nums2_Index = 0
  
  while nums2_Index < len(nums2):
    if (nums2[nums2_Index] >= nums1[nums1_Index]):
      #insert nums2[nums2_Index] into nums1[nums1_Index]
      # remove an element at the end of the list (aka del nums1[len(nums1)-nums1Index]
      nums2_Index+=1 
    else:
      nums1_Index +=1 
      
      