def threeSum( nums):
    nums_dict = {}
    nums.sort()
    print("sorted nums: ", nums)
    for i, item in enumerate(nums):
        nums_dict[item]=i

    print(nums_dict)
    triplets_strlist = []       
    for index_a in range(len(nums)):
        print("a ", nums[index_a])
        for index_b in range(index_a+1, len(nums)):
            print("b ", nums[index_b])
            item_c = -(nums[index_a] + nums[index_b])
            if item_c in nums_dict and \
                nums_dict[item_c] > index_b:
                triplets_strlist.append(",".join([str(nums[index_a]), str(nums[index_b]), str(item_c)]))
                print("triplest_list: ", triplets_strlist)
                print("triplets: ", [nums[index_a], nums[index_b], item_c])
    triplets_strlist = list(set(triplets_strlist))
    triplets_intlist = [item.split(",") for item in triplets_strlist]
    return triplets_intlist

output = threeSum([-1,0,1,2,-1,-4])
print(output)