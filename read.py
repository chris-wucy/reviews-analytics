# 讀取檔案：
def read_file(filename):
	with open(filename, 'r') as f:
		data = []
		count = 0
		for line in f:
			data.append(line)
			count += 1
			if count % 1000 == 0: # % 是求餘數
				print(len(data))
			# 把進度印出來，但print很花時間，所以每1000筆印一次
	return data
	print('檔案讀取完了, 總共有', len(data), '筆資料')
	#print(data[0])

# command + / 
# -------------------- 
def sum_len(data):
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


# # 清單篩選快寫法：

# good = [d for d in data if 'good' in d]
# # 第一個d代表原封不動放進good
# # good = [1 for d in data if 'good' in d]
# # 改成1的話會把1放進good裡，滿滿的1

# bad = []
# for d in data:
# 		bad.append('bad' in d)

# # 快寫法：
# bad = ['bad' in d for d in data]
# # 每一個在data裡的都做 'bad' in d 的判斷，True or False
# print(bad)

# 算各個字出現的次數，用字典
def counts(data):
	wc = {} # word_count
	for d in data:
		words = d.strip().split() # split拿掉' ', 用預設值，就不會出現空字串
		for word in words:
			if word in wc: # 沒有的話可以用not in
				wc[word] += 1
			else:
				wc[word] = 1 # 沒有就設成1，第1次出現
	for word in wc:
		if wc[word] > 1000000:
			print(word, wc[word])	
	print(len(wc))

	while True:
		word = input('請問您想查什麼字： ')
		if word == 'q':
			break
		if word not in wc:
			print('查無此字')
		print(word, '出現過的次數為：', wc[word])
	print('感謝使用本查詢功能')


def main():
	data = read_file('reviews.txt')
	sum_len(data)
	counts(data)

main()

# 使用者輸入想查某個字出現的次數

#print(good[0])
#print(new[1])