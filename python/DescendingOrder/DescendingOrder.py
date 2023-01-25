# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

#Examples:
#Input: 42145 Output: 54421

#Input: 145263 Output: 654321

#Input: 123456789 Output: 987654321

def descending_order(num):
    desc_list = [int(x) for x in str(num)]
    
    for i in range(0, len(desc_list)):
        desc_list[i] = int(desc_list[i])
        desc_list.sort(reverse = True)
        
    return int(''.join(str(i) for i in desc_list))
