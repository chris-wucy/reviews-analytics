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
	# print(sum_len)
print('分析完畢！平均每筆資料長度為：', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言長度小於100')





# 清單篩選快寫法：

good = [d for d in data if 'good' in d]
# 第一個d代表原封不動放進good
# good = [1 for d in data if 'good' in d]
# 改成1的話會把1放進good裡，滿滿的1

bad = []
for d in data:
		bad.append('bad' in d)

# 快寫法：
bad = ['bad' in d for d in data]
# 每一個在data裡的都做 'bad' in d 的判斷，True or False
print(bad)


#print(good[0])
#print(new[1])