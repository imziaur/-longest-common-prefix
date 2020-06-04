def longestCommonPrefix( a): 
      
    size = len(a) 
  
    # retun 0 if no input found  
    if (size == 0): 
        return "" 
  
    if (size == 1): 
        return a[0] 
  
    # sort the array of strings  
    a.sort() 
      
    # find the minimum length from  
    # first and last string  
    end = min(len(a[0]), len(a[size - 1])) 
  
    # find the common prefix between  
    # the first and last string  
    i = 0
    while (i < end and 
           a[0][i] == a[size - 1][i]): 
        i += 1
  
    pre = a[0][0: i] 
    # return -1, if no match found
    if (len(pre)<1):
        return -1
    
    return pre

if __name__ == "__main__": 
  
    input = ["Cards", "Cars", "Caffeine", "Cardiology"] 
    print("The longest Common Prefix is :" , 
                 longestCommonPrefix(input))

