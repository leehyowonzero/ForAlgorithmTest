html = input()
divide = html.split('<div title="')
for i in range(1, len(divide)):
	div = divide[i]
	p_list = div.split('<p>')
	title = p_list.pop(0)
	title = title[:-2]
	print('title :', title)

	for ps in p_list:
		sentence = ''
		j = 0
		while j < len(ps):
			if ps[j] == '<':
				for k in range(j+1, len(ps)):
					if ps[k] == '>':
						j = k
						break
			else:
				sentence += ps[j]
			j += 1
		sentence = ' '.join(sentence.split())
		print(sentence)