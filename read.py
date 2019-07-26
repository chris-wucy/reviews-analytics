data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 是求餘數
			print(len(data))
			# 把進度印出來，但print很花時間，所以每1000筆印一次
print(len(data))
print(data[0])
print('-------------------')
print(data[1])