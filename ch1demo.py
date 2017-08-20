

f = open('weather_info.txt','r',encoding = 'utf-8')

data = f.read()

#读取文档

a = []
weather_data = {}
#由于要用split两次，来得到一个list所以通过a来赋值给weather_data


for line in data.splitlines(): #调试发现用split('\n')最后一个会有空字典，读文档看到这个函数
	 a = line.split(',')
	 city = a[0]
	 weather = a[1]
	 weather_data[city] = weather

print("请输入指令或者城市名字：")


history = []

while True:
	user_input =input('> ')
	if user_input == 'quit' or user_input == 'q':
		exit(0)
	
	elif user_input == 'help' or user_input == '?':
		print('''
		输入城市名，查询该城市天气；
		输入 help，获取帮助文档；
		输入 history，获取查询历史；
		输入 quit，退出天气查询系统。
		''')
		
	elif user_input in weather_data:
		print(f"{user_input}  {weather_data[user_input]}")
		history.append(f"{user_input}  {weather_data[user_input]}")
	
	elif user_input == 'history':
		print(history)
	
	else:
	    print("对不起没有该地方天气资料")

