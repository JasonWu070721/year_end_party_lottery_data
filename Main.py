import numpy as np
import random
import json

line_num = 1
test_num = 300
people_matrix_size = 8
random_max_num = people_matrix_size * people_matrix_size
people_count = 20
lottery_max_num = 64 # people_matrix_size * people_matrix_size

people_all_matrix = np.zeros(shape=(people_count, people_matrix_size, people_matrix_size), dtype=int)
lottery_random_list = list(range(0, lottery_max_num))


def write_matrix_json(data, name):
	json_string = json.dumps(data)
	# print(json_string)

	with open(f"data/{name}.json", 'w') as outfile:
		outfile.write(json_string)

def set_people_matrix():
	for people in range(0, people_count):
		people_random_list = list(range(0, random_max_num))
		random.shuffle(people_random_list)

		write_matrix_json(people_random_list, people)

		conunt_list = 0
		for i in range(0, people_matrix_size):
			for j in range(0, people_matrix_size):
				people_all_matrix[people][i][j] = people_random_list[conunt_list]
				conunt_list = conunt_list + 1

def get_lottery_count():

	random.shuffle(lottery_random_list)

	lottery_count = 0
	for lottery in lottery_random_list:
		# print("lottery: ", lottery)
		for people in range(0, people_count):
			# print("people: ", people)
			for i in range(0, people_matrix_size):
				for j in range(0, people_matrix_size):
					if people_all_matrix[people, i, j] == lottery:
						 people_all_matrix[people, i, j] = -1

			# Row
			for i in range(0, people_matrix_size):
				line_count = 0
				for j in range(0, people_matrix_size):

					if people_all_matrix[people, i, j] == -1:
						line_count = line_count + 1

					if line_count >= people_matrix_size:
						print(people_all_matrix[people])
						print("lottery_count: ", lottery_count)
						return lottery_count

			# Column
			for i in range(0, people_matrix_size):
				line_count = 0
				for j in range(0, people_matrix_size):

					if people_all_matrix[people, j, i] == -1:
						line_count = line_count + 1

					if line_count >= people_matrix_size:
						print(people_all_matrix[people])
						print("lottery_count: ", lottery_count)
						return lottery_count


			# diagonal
			line_count = 0
			people_diagonal = np.diagonal(people_all_matrix[people])

			for diagonal in people_diagonal:
				if diagonal == -1:
					line_count = line_count + 1

				if line_count >= people_matrix_size:
					print(people_all_matrix[people])
					print("lottery_count: ", lottery_count)
					return lottery_count

			# flip and diagonal
			people_flip = np.flip(people_all_matrix[people], axis=1)
			line_count = 0
			people_diagonal = np.diagonal(people_flip)

			for diagonal in people_diagonal:
				if diagonal == -1:
					line_count = line_count + 1

				if line_count >= people_matrix_size:
					print(people_all_matrix[people])
					print("lottery_count: ", lottery_count)
					return lottery_count

		lottery_count = lottery_count + 1



lottery_count_all = []
for test_run in range(0, test_num):
	set_people_matrix()
	lottery_count = get_lottery_count()
	lottery_count_all.append(lottery_count)
	lottery_count_all.sort()

print(lottery_count_all)

