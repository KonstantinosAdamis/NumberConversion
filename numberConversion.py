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

	print(list(reversed(digit_arr)))

binary(4)
binary(544)
binary(4006)

def decimal(b_num):

	s = 0

	j = len(b_num) - 1

	for i in range(len(b_num)):

		s += int(b_num[i])*(2**j)

		j -= 1

	print(s)

decimal("11")
decimal("10010")
decimal("111001110101")
