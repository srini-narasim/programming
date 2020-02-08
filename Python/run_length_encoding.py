#RLE(Run Length Encoding) for lossless data compression
#Algorithm of RLE - replace runs with some representation of what was repeated and how many times it was 
#					repeated in the original list

#Replace each subsequence with the following:
#the letter D, the digit repeated, how many were there originally

def calculate_RLE(list):
	count = 0
	new_list =[]
	for i in list: 
		if i not in new_list:
			new_list.append(i)
		else:
			count += 1

	if count >= 3:
		new_list.append("D")
		new_list.append(count + 1)
	return new_list

print calculate_RLE([3,2,2,2,2,2,2,5,6])

#Output: [3, 2, 5, 6, 'D', 6]