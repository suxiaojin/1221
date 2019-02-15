import os
import sys
if os.getuid()==0:
    pass
else:
    print("请以root登录")

version=input("请输入你想安装的python版本2.7/3.5")
if  version=='2.7':
    url="https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz"
elif version=='3.5':
    url="https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz"
else:
    print('您输入的版本号有误，请输入2.7或3.5')
    sys.exit(1)

cmd='wget' +' '+ url
res=os.system(cmd)
if res!=0:
    print('下载源码包失败')
    sys.exit(1)

if  version=='2.7':
    package_name='Python-2.7.12.tgz'
else:
    package_name='Python-3.5.2.tgz'
cmd='tar xf' +' '+ package_name + '.tgz'
res=os.system(cmd)
if res!=0:
    os.system('rm'+package_name+'.tgz')
    print('解压源码包失败，重新下载')
    sys.exit(1)

cmd='cd'+' '+package_name+'&& ./configure --prefix=/usr/local/python && make && make install'
res=os.system(cmd)
if res!=0:
    print('编译源码失败')
    sys.exit(1)

