# -- coding: utf-8 --
#ch0 教练的评价是让我多写注释，好吧，为了养成习惯，我决定在所有的的程序中添加这一句
#张勰嵩写代码要写注释！不写注释你怎么学会代码！怎么去做程序员啊！

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}


cities = {
	'CA':'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}	

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 上面设置了两个字典，一个是州名与对应的州名缩写 州名缩写与对应城市

print('-' * 10)
print("NY State has: ",cities['NY'])
print("OR State has: ",cities['OR'])
#输出一些字典里面的内容

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ",cities[states['Florida']])

#嵌套使用，这里其实展现了如何用参数来调用cities里面的的内容，如果设置一个参数=state[]

print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
# 用items()遍历states这个字典 把变量名字和对应值传回
#然后用 list转换成列表 然后for循环输出

print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")
	
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")
	
print('-' * 10)
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")
# get 用得到键去查找参数，如果没有返回0也就是否 所以NOT 否 就执行print	
city = cities.get('TX','Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
#更简洁的写法，get函数里面直接把返回值设定为输出语句







