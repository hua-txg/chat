

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines 

def convert(lines):
	person = None
	allen_word_conut = 0
	viki_word_conut = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				allen_word_conut += len(m)
		elif name == 'Viki':
			for m in s[2:]:
				viki_word_conut += len(m)
	print('allen說了', allen_word_conut)
	print('viki說了', viki_word_conut)

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()
