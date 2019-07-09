def merge_sorted_lists(nums1, nums2):

  nums1 = [1,2,3,0,0,0]
  nums2 = [2,5,6]
  # modify num1 in-place
  nums1_Index = 0
  nums2_Index = 0
  while nums2_Index < len(nums2) :
    if (nums2[nums2_Index] <= nums1[nums1_Index]) or nums1_Index ==0:
      nums1.insert(nums1_Index, nums2[nums2_Index])
      nums1.pop()
      nums2_Index+=1 
    else:
      nums1_Index +=1 
  
