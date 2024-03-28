data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(len(data))
print(data[0])
print('檔案讀取完了，總共有', len(data), '筆資料')

wc = {}  #word_conut
for d in data:
	words = d.split()  #將d用空格切割存到words
	for word in words:
		if word in wc:
			wc[word] +=1  #word在字典裏，將key  word的值+1
		else:
			wc[word] = 1  #word不在字典裏，新增新的key寫入字典 { word:1 }

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])  #印出字及出現的次數
		# print(wc['Allen'])

	# print(wc)
while True:
	word = input('請問你想查什麼字')
	if word == 'q':
		break
	print(word, '出現過的次數為：', wc[word])
print('感謝使用')









# #計算平均留言的長度，將每一筆留言的長度sum計算出來，除以留言筆數，就是留言的平均長度
# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# print('留言的平均長度為', sum_len/len(data))

# #篩選出每筆留言小於100個字
# new = []
# for d in data:  #d是一個留言
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')
# print(new[0])

# #篩選出每筆留言包含 good
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])

# #list comprehension 清單快寫法
# good = [d for d in data if 'good' in d  ]
# print('list comprehension 清單快寫法 一共有', len(good), '筆留言提到good')

# bad = ['bad' in d for d in data]
# print(bad)





