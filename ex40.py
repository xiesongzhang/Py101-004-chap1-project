# -- coding: utf-8 --
#张勰嵩写代码要写注释！不写注释你怎么学会代码！怎么去做程序员啊！

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
#line 是局部变量 self.lyrics是实列化？但是为什么要这样写？还是不太明白
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
#以上是两个实列化，Song 是class里面已经定义的函数
happy_bday.sing_me_a_song()

#用.这个命令去调用类里面的sing_me_a_song()函数

bulls_on_parade.sing_me_a_song()