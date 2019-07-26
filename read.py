data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 是求餘數
			print(len(data))
			# 把進度印出來，但print很花時間，所以每1000筆印一次
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for dat in data:
	sum_len += len(dat)
	#print(sum_len)
print('分析完畢！平均每筆資料長度為：', sum_len/len(data))
