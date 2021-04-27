from timeit import default_timer as timer
from colorama import Fore, init
from patterns import patterns

def main():
	with open('input.txt', 'r') as input_file:
		words = input_file.read().strip().split('\n')
	out = []
	start_time = timer()

	for word in words:
		key = ''.join(sorted(word.lower()))
		out.append('%s: %s' % (
			word,
			', '.join(patterns[key]) if key in patterns else ''
		))

	end_time = timer()
	init()
	print('\n'.join(out))

if __name__ == '__main__':
	main()
