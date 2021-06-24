#!/usr/bin/python3

# 打开文件
fo = open("lucas.txt", "r+")
print ("文件名: ", fo.name)

str = "6:www.runoob.com"
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write( str )

# 读取文件所有内容
fo.seek(0,0)
for index in range(6):
    line = next(fo)
    print ("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()

******************************************************
文件名:  lucas.txt
文件行号 0 - 1:www.runoob.com

文件行号 1 - 2:www.runoob.com

文件行号 2 - 3:www.runoob.com

文件行号 3 - 4:www.runoob.com

文件行号 4 - 5:www.runoob.com

文件行号 5 - 6:www.runoob.com
