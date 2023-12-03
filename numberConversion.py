b_num = input("Give a binary number: ")

s = 0

j = len(b_num) - 1

for i in range(len(b_num)):

	s += int(b_num[i])*(2**j)

	j -= 1

print(s)

d_num = int(input("Give a decimal number: "))

def binary(d_num):

	digit_arr = []
		
	if d_num == 0:

		digit_arr = [0]

	while d_num != 0:

		if (d_num % 2) == 0:

			digit_arr.append(0)

		else:

			digit_arr.append(1)

		d_num //= 2

	return (list(reversed(digit_arr)))

print(binary(d_num))
