def merge_sort(array):
    if len(array)<=1:
        return array
    else:
        ret=[]
        half = len(array)/2
        lower = merge_sort(array[:half])
        upper = merge_sort(array[half:])
        lower_len = len(lower)
        upper_len = len(upper)

        i=0
        j=0
        while i != lower_len or j != upper_len:
            if(i != lower_len and (j == upper_len or lower[i] < upper[j])):
                ret.append(lower[i])
                i += 1
            else:
                ret.append(upper[j])
                j += 1

        return ret 


array=[4,2,3,8,7,6,9,0]*100000

merge_sort(array)

