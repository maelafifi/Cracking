NUM_PERMUTAITONS = ['1','2','3','4','5','6','7','8','9']

def first_to_last(first, last, filename):
	first_and_last = first+last
	with open('number_permutations', 'r') as f:
		with open('test.txt', 'a') as o:
			o.write(first "\n")
			o.write(last + '\n')
			o.write(first_and_last)
			for permutation in f.readlines():
				o.write(first_and_last+permutation)


def gen_single(NUM_PERMUTAITONS):
	for l in NUM_PERMUTAITONS:
		print l


def gen_doubles(NUM_PERMUTAITONS):
	for l in NUM_PERMUTAITONS:
		for m in NUM_PERMUTAITONS:
			print l+m

def gen_triples(NUM_PERMUTAITONS):
	for l in NUM_PERMUTAITONS:
		for m in NUM_PERMUTAITONS:
			for n in NUM_PERMUTAITONS:
				print l+m+n

def gen_fours(NUM_PERMUTAITONS):
	for l in NUM_PERMUTAITONS:
		for m in NUM_PERMUTAITONS:
			for n in NUM_PERMUTAITONS:
				for o in NUM_PERMUTAITONS:
					print l+m+n+o

def main():
	# Pipe into file to use
	# gen_single(NUM_PERMUTAITONS)
	# gen_doubles(NUM_PERMUTAITONS)
	# gen_triples(NUM_PERMUTAITONS)
	# gen_fours(NUM_PERMUTAITONS)
	filename = 'number_permutations'
	first = raw_input("What's your first name? ")
	last = raw_input("What's your last name? ")
	# sport = raw_input("What's your favorite sport? ")
	# animal = raw_input("What's your favorite animal? ")
	first_to_last(first,last, filename)

if __name__ == '__main__':
	main()