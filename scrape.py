import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

xs = []
zs=[]
rahul=0
qual=0
diff = 0
ys = []
def animate(i):
	global diff
	res = requests.get(url, cookies=cookies)

	#print(r.content)
	soup_data = BeautifulSoup(res.text, 'html.parser')
	#print(soup_data.title)
	print("\n")
	#print(soup_data)
	x=soup_data.find_all("div", class_="pds-feedback-group")
	for t in x:
		name = t.findAll("span", {"class": "pds-answer-text"})[0].string
		votes = t.findAll("span", {"class": "pds-feedback-votes"})[0].string
		#print(name)
		votes_str = (votes.replace(",", "").replace("(", "").replace(")", "").replace("  ", "").replace("votes", ""))
		val=int(votes_str)
		if name == "Rakuten's Rahul Atri":
			rahul=val
		elif name=="Qualcomm's Ozge Koymen":
			qual=val
		#print(val)
	print("Difference "+ str(rahul-qual))
	print("Rate "+ str((rahul-qual - diff)/5))
	diff = rahul-qual
	xs.append(time.strftime('%H:%M:%S'))
	ys.append(diff)
	ax1.clear()
	ax1.plot(xs, ys)
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
url = 'https://poll.fm/10619136'
cookies = {"pd-captcha_poll_AC614EC2581FF90C97CE85780CBB59BD": "03AGdBq257-i6fwJMCZzWtHzCZhfsU70gJCTrC8XyNZfqg1uHCupzHP4teK9aLr8B65ocYN-c7Ov4n1_bv4AYu4k4wR-QvLv_PeaoFbUTpWXFEeAor6SHeUkfSJFTgz9MhqlP_ZQIJyJ1QsL62ecXgUPxqHZ6d60jkSL_Ws12nMRlL3CDiGcUErlu7rJeEmbpLs-seWqXuNXpy2NSU3JnV8TfG3699akZryQW8FiG561gu1RNHOt0z1uDAQSM0C8fHu9Rc5VOVh8q89mdjweC8o0HxyyU2mQ1cr5Q86baUkujzkC4oMRUfPVD1bHkrYqXUQzf-tHahPi-vT7pmm9b3gl2d85PCNOiEEuw9IJO_yYwVb4lSiLNNY7Vc6u2KcwRa9EWLQ5dMLj-gzgki9fmwSo2PyMOd88NgWH65CqM1sfU_3Lpygtm7w0Aw04g9GY3g5Wmmp0t39BnqkdyKRh6jG239NxzMS8D0wNoNF8tMHtXKYcLMj_eaUF1h8xgOdm9ve7GMwLhrIzG3"}
cookies["PD_poll_10619136"]="1602408846"
cookies["PD_REQ_AUTH"]="ce93ef7d00efaf5aac58d20e792ae8f8"
cookies["PDjs_poll_10619136"]="1602408846111"
res = requests.get(url, cookies=cookies)

#print(r.content)
soup_data = BeautifulSoup(res.text, 'html.parser')
print(soup_data.title)
print("\n")
#print(soup_data)
x=soup_data.find_all("div", class_="pds-feedback-group")

for t in x:
	name = t.findAll("span", {"class": "pds-answer-text"})[0].string
	votes = t.findAll("span", {"class": "pds-feedback-votes"})[0].string
	#print(name)
	votes_str = (votes.replace(",", "").replace("(", "").replace(")", "").replace("  ", "").replace("votes", ""))
	val=int(votes_str)
	if name == "Rakuten's Rahul Atri":
		rahul=val
	elif name=="Qualcomm's Ozge Koymen":
		qual=val
	#print(val)
diff = rahul-qual
ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()