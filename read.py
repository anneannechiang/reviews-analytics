data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Finish reading, and the total lines are', len(data),'.')

sum_len = 0
for d in data:
	sum_len += len(d)
print('The average message length is', sum_len/len(data),'.')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('Note 1:', len(new), 'messages (length is lower than 100).')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('Note 2:', len(good), 'messages mentioned "good".')

# word count
wc = {} 
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # add new key into wc dictionary
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('What word do you want to search..? ')
	if word == 'q':
		break
	if word in wc:
		print(word, ': it appears', wc[word], 'times.')
	else:
		print(word, ': it has not appeared yet..')

print('Good-bye!')





