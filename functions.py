from map import *
from msvcrt import getch
import os
clear = lambda: os.system('cls')

def initialize_menu(key_up, key_down, key_left, key_right, key_enter):
	start = ['                                      start', '                                    > start <']
	options = ['                                     options', '                                   > options <']
	quit = ['                                       quit', '                                     > quit <']
	choice = [start[1], options[0], quit[0]]

	while True:
		print('\n' * 9)
		print(title_maze[0])
		print('\n')
		print(title_game[0])
		print('\n' * 3)
		print(choice[0])
		print(choice[1])
		print(choice[2])
		print('\n' * 9)
		print('press', key_up, 'to go up, press', key_down, 'to go down, press', key_enter, 'to select')
		userinput = str(list(str(getch()))[2])
		if userinput == key_down:
			if choice[0] == start[1]:
				choice[0] = start[0]
				choice[1] = options[1]
			elif choice[1] == options[1]:
				choice[1] = options[0]
				choice[2] = quit[1]
			elif choice[2] == quit[1]:
				choice[2] = quit[0]
				choice[0] = start[1]
		elif userinput == key_up:
			if choice[0] == start[1]:
				choice[0] = start[0]
				choice[2] = quit[1]
			elif choice[1] == options[1]:
				choice[1] = options[0]
				choice[0] = start[1]
			elif choice[2] == quit[1]:
				choice[2] = quit[0]
				choice[1] = options[1]
		elif userinput == key_enter:
			if choice[0] == start[1]:
				initialize_game(key_up, key_down, key_left, key_right, key_enter)
			elif choice[1] == options[1]:
				key_up, key_down, key_left, key_right, key_enter = initialize_options(key_up, key_down, key_left, key_right, key_enter)
			elif choice[2] == quit[1]:
				clear()
				exit()
		clear()

def initialize_options(key_up, key_down, key_left, key_right, key_enter):
	up    = ['                                  up     =     ', '                                > up     =     ', key_up]
	down  = ['                                  down   =     ', '                                > down   =     ', key_down]
	left  = ['                                  left   =     ', '                                > left   =     ', key_left]
	right = ['                                  right  =     ', '                                > right  =     ', key_right]
	enter = ['                                  enter  =     ', '                                > enter  =     ', key_enter]
	back  = ['                                  back to menu ', '                                > back to menu']
	choice = [up[1], down[0], left[0], right[0], enter[0], back[0]]

	while True:
		print('\n' * 5)
		print('                                  CONTROLS')
		print('\n' * 4)
		print(choice[0], up[2])
		print(choice[1], down[2])
		print(choice[2], left[2])
		print(choice[3], right[2])
		print(choice[4], enter[2])
		print('\n' * 2)
		print(choice[5])
		print('\n' * 23)
		userinput = str(list(str(getch()))[2])
		if userinput == down[2]:
			if choice[0] == up[1]:
				choice[0] = up[0]
				choice[1] = down[1]
			elif choice[1] == down[1]:
				choice[1] = down[0]
				choice[2] = left[1]
			elif choice[2] == left[1]:
				choice[2] = left[0]
				choice[3] = right[1]
			elif choice[3] == right[1]:
				choice[3] = right[0]
				choice[4] = enter[1]
			elif choice[4] == enter[1]:
				choice[4] = enter[0]
				choice[5] = back[1]
			elif choice[5] == back[1]:
				choice[5] = back[0]
				choice[0] = up[1]
		elif userinput == up[2]:
			if choice[0] == up[1]:
				choice[0] = up[0]
				choice[5] = back[1]
			elif choice[1] == down[1]:
				choice[1] = down[0]
				choice[0] = up[1]
			elif choice[2] == left[1]:
				choice[2] = left[0]
				choice[1] = down[1]
			elif choice[3] == right[1]:
				choice[3] = right[0]
				choice[2] = left[1]
			elif choice[4] == enter[1]:
				choice[4] = enter[0]
				choice[3] = right[1]
			elif choice[5] == back[1]:
				choice[5] == back[0]
				choice[4] == enter[1]
		elif userinput == enter[2]:
			if choice[0] == up[1]:
				print('\n' * 5)
				print('                                  CONTROLS')
				print('\n' * 4)
				print(choice[0], '_')
				print(choice[1], down[2])
				print(choice[2], left[2])
				print(choice[3], right[2])
				print(choice[4], enter[2])
				print('\n' * 2)
				print(choice[4])
				print('\n' * 24)
				up[2] = str(list(str(getch()))[2])
			elif choice[1] == down[1]:
				print('\n' * 5)
				print('                                  CONTROLS')
				print('\n' * 4)
				print(choice[0], up[2])
				print(choice[1], '_')
				print(choice[2], left[2])
				print(choice[3], right[2])
				print(choice[4], enter[2])
				print('\n' * 2)
				print(choice[4])
				print('\n' * 24)
				down[2] = str(list(str(getch()))[2])
			elif choice[2] == left[1]:
				print('\n' * 5)
				print('                                  CONTROLS')
				print('\n' * 4)
				print(choice[0], up[2])
				print(choice[1], down[2])
				print(choice[2], '_')
				print(choice[3], right[2])
				print(choice[4], enter[2])
				print('\n' * 2)
				print(choice[4])
				print('\n' * 24)
				left[2] = str(list(str(getch()))[2])
			elif choice[3] == right[1]:
				print('\n' * 5)
				print('                                  CONTROLS')
				print('\n' * 4)
				print(choice[0], up[2])
				print(choice[1], down[2])
				print(choice[2], left[2])
				print(choice[3], '_')
				print(choice[4], enter[2])
				print('\n' * 2)
				print(choice[4])
				print('\n' * 24)
				right[2] = str(list(str(getch()))[2])
			elif choice[4] == enter[1]:
				print('\n' * 5)
				print('                                  CONTROLS')
				print('\n' * 4)
				print(choice[0], up[2])
				print(choice[1], down[2])
				print(choice[2], left[2])
				print(choice[3], right[2])
				print(choice[4], '_')
				print('\n' * 2)
				print(choice[4])
				print('\n' * 24)
				enter[2] = str(list(str(getch()))[2])
			elif choice[5] == back[1]:
				break
	return up[2], down[2], left[2], right[2], enter[2]

def initialize_game(key_up, key_down, key_left, key_right, key_enter):
	win = False
	current = 41
	
	while True:
		clear()
		for value in maze:
			print(value, end='')
		print('press', key_up, 'to go up, press', key_down, 'to go down, press', key_left, 'to go left, press', key_right, 'to go right')
		userinput = str(list(str(getch()))[2])
		if userinput == key_up and maze[current - 41] == '  ':
			maze[current - 41] = '░░'
			maze[current] = '  '
			current = current - 41
		elif userinput == key_down and maze[current + 41] == '  ':
			maze[current + 41] = '░░'
			maze[current] = '  '
			current = current + 41
		elif userinput == key_left and maze[current - 1] == '  ':
			maze[current - 1] = '░░'
			maze[current] = '  '
			current = current - 1
		elif userinput == key_right and maze[current + 1] == '  ':
			maze[current + 1] = '░░'
			maze[current] = '  '
			current = current + 1
		if current == 1639:
			break

	clear()
	print('\n' * 20)
	print('                                     you win')
	print('\n' * 20)
	exit()
