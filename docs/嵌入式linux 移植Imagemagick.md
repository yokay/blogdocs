> 项目中遇到图片转换，需要图片另存为功能.  

通过查阅资料，**Imagemagick** 的**convert**命令工具可以实现图片转换；但是需要把**Imagemagick** 工具移植到嵌入式linux系统中；  



## libbz2 库的交叉编译及移植

**Imagemagick** 采用的是*ImageMagick-7.0.10-30*，依赖**libbz2.so.0**;所以先在ubuntu 14.0系统上交叉编译**libbz2**库。  

### 下载bzip2-1.0.6.tar.zip

下载路径[^1][^2]

​        

### 交叉编译参考

#### 网上的例子[^3]

在arm平台下使用**boost**库.

##### 修改Makefile文件

```shell
SHELL=/bin/bash

To assist in cross-compiling

CC=/home/frp/code/third_libs/gcc-linaro-7.3.1-2018.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc
AR=/home/frp/code/third_libs/gcc-linaro-7.3.1-2018.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-ar
RANLIB=/home/frp/code/third_libs/gcc-linaro-7.3.1-2018.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-ranlib
LDFLAGS=

BIGFILES=-D_FILE_OFFSET_BITS=64
CFLAGS=-Wall -Winline -O2 -g $(BIGFILES)

Where you want it installed when you do 'make install'

PREFIX=/home/frp/code/third_libs/bzip2-1.0.6/install

OBJS= blocksort.o  \
      huffman.o    \
      crctable.o   \
      randtable.o  \
      compress.o   \
      decompress.o \
      bzlib.o

all: libbz2.a bzip2 bzip2recover

bzip2: libbz2.a bzip2.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o bzip2 bzip2.o -L. -lbz2

bzip2recover: bzip2recover.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o bzip2recover bzip2recover.o
```

使用bzip2-1.0.6版本,上面的代码为Makefile文件中的部分(修改后的).

修改了SHELL=后的sh为bash,不修改的话会报如下错误:

```
Doing 6 tests (3 compress, 3 uncompress) …
If there’s a problem, things might stop at this point.
./bzip2 -1 < sample1.ref > sample1.rb2
./bzip2: 1: ./bzip2: Syntax error: word unexpected (expecting “)”)
Makefile:57: recipe for target ‘test’ failed
make: *** [test] Error 2
```

修改CC=,AR=,RANLIB=为实际的交叉编译链中gcc,ar,ranlib的路径
修改PREFIX=为要安装位置,如果默认的话可能会覆盖系统的这些库(没试过)
去掉all后面的test,测试老是不通过,猜想可能是于实际平台不符导致的

#### 项目实战

需要先把交叉编译环境source 

然后修改交叉编译链 

```shell
CC=arm-oe-linux-gnueabi-gcc
AR=arm-oe-linux-gnueabi-ar
RANLIB=arm-oe-linux-gnueabi-ranlib
```

修改PREFIX=  



去掉test: bzip2后面的
然后操作 make ;make stall

**这个操作是编译静态库。**



1. 修改Makefile-libbz2_so
2. 修改CC=arm-oe-linux-gnueabi-gcc
3. 修改动态库为libbz2.so.0 链接库 libbz2.so.0.1
4. 执行make -f Makefile-libbz2_so 编译动态库

编译安装 make&make install
将libbze.so.0拷到到终端/usr/lib 下

**这个操作是生成动态库。**



## Imagemagick交叉编译移植[^4][^5]

  先执行source,导出交叉编译工具，然后 执行以下命令

```shell
tar -xzvf ImageMagick.tar.gz
cd ImageMagick
mkdir build
cd build   

../configure --prefix=$PWD/__install --disable-installed --without-perl --without-x --without-fpx --without-wmf --disable-openmp --host=arm-oe-linux-gnueabi
make
make install
```

测试如下：

在build/install/bin目录下拷贝convert magick工具到终端/usr/bin
在build/install/lib目录下拷贝  libMagickCore-7.Q16HDRI.so.7 libMagickWand-7.Q16HDRI.so.7两个库到终端/usr/lib目录下
测试 convert 4.jpg 5.jpg



## Reference

[^1]: [bzip2-1.0.6.tar.zip](https://www.onlinedown.net/soft/169551.html)
[^2]: [bzip2-1.0.6.tar.zip](http://www.bzip.org/downloads.html)
[^3]: [交叉编译参考](https://blog.csdn.net/a119258/article/details/103888209)
[^4]: [Imagemagick交叉编译移植](https://www.cnblogs.com/dakewei/p/7471679.html)
[^5]: [ImageMagick.tar.gz](https://github.com/ImageMagick/ImageMagick.git)

