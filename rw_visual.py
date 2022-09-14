import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
#创建一个RadndomWalk实例
	rw = RandomWalk()
	rw.fill_walk()
	
	#绘制出所有点
	plt.style.use('classic')
	fig, ax = plt.subplots()
	ax.scatter(rw.x_values, rw.y_values, s=15)

	#隐藏坐标轴
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("another run? (y/n):")
	if keep_running == 'n':
		break