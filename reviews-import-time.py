import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 1000 == 0: 
		# 	print(len(data))   #每讀取1000筆就印出一次
		bar.update(count)

# print(len(data))

# print(data[0])
print('檔案讀取完了，總共有', len(data), '筆資料')

#計算平均留言的長度，將每一筆留言的長度sum計算出來，除以留言筆數，就是留言的平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))

#篩選出每筆留言小於100個字
new = []
for d in data:  #d是一個留言
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

#篩選出每筆留言包含 good
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

#list comprehension 清單快寫法
good = [d for d in data if 'good' in d  ]
print('list comprehension 清單快寫法 一共有', len(good), '筆留言提到good')

bad = ['bad' in d for d in data]
# print(bad)


#文字計數
#計花費時間
start_time = time.time()

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

end_time = time.time()
print('花了', end_time - start_time, 'seconds')

	# print(wc)
while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒有出現過喔!')  #避開查無此字而造成當機的問題

	print('感謝使用')







