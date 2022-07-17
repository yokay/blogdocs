## 一、基本概念

先来明确几个概念。

### 1.1 物理地址和逻辑地址

物理地址就是存储单元的绝对地址，逻辑地址往往是物理地址基础上加一个偏移量，即逻辑地址零 = 物理地址零 + 偏移。

### 1.2 MBR 和 DBR

MBR：英语全称是 Master Boot Record，即主引导记录。

DBR：英语全称是 Dos Boot Record，即 DOS 引导记录，也称为操作系统引导记录。

### 1.3 扇区和簇

一个扇区一般分为 512 字节、1024 字节、2048 字节和 4096 字节。

一个簇一般包含 1、2、4、8、16、32、64 和 128 个扇区。

## 二、FAT32 文件系统的结构

先从整体上把握 FAT32 文件系统的结构，如图 1 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_01_FAT32_Structure.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_01_FAT32_Structure.png)图 1 FAT32 文件系统整体结构

从上图可以看出，FAT32 文件系统结构由隐藏扇区（MBR 等）、保留扇区（DBR 等）、FAT 和数据区等几个部分组成，下面就详细分析一下各个部分的实际意义。

### 2.1 MBR 分析

已格式化为 FAT32 格式后，从物理地址零开始的 512 个字节是 MBR(Master Boot Record)，即主引导记录。其中的前 446 个字节为引导代码，我们这里不做详解。接下来的 64 个字节为分区表，其中 16 个字节为一组总共四组，每一个组都描述了一个分区，最后两个字节为固定的末尾签名，0x55、0xAA。如图 2 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_02_FAT32_MBR.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_02_FAT32_MBR.png)

图 2 FAT32 文件系统 MBR

图 2 中，从物理地址的 0x0000 至 0x01BD 的 446 字节为引导代码，从 0x01BE 至 0x01CD 的 16 字节指示了一个分区（黑色框），其中，0x01C6 至 0x01C9 的 4 字节指示了逻辑扇区 0 的位置（红色框），也就是 DBR 的位置，在物理扇区 0x0000 003F （63）处。

接下来看 DBR 的内容。

### 2.2 DBR 分析

DBR 部分由跳转指令、OEM ID、BPB（BIOS 参数）、拓展 BPB、引导程序和结束标志组成，如图 3 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_03_FAT32_DBR.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_03_FAT32_DBR.png)

图 3 FAT32 文件系统 DBR

-   跳转指令将呈现执行流程跳转到引导程序处；
-   OEM ID 由厂商指定，这里是 MSDOS5.0；
-   BPB 记录文件系统相关的重要信息，由 BPB 和拓展 BPB 组成，BPB 具体参数解释如下：

| 字节位移 | 字段长度(字节) | 图 3 对应取值      | 名称和定义                                                   |
| -------- | -------------- | ------------------ | ------------------------------------------------------------ |
| 0x0B     | 2              | 0x0200             | 扇区字节数(Bytes Per Sector) 硬件扇区的大小。本字段合法的十进制值有 512、1024、2048 和 4096。对大多数磁盘来说，本字段的值为 512。 |
| 0x0D     | 1              | 0x40               | 每簇扇区数(Sectors Per Cluster)。FAT32 文件系统只能跟踪有限个簇(最多为 4 294 967 296 个)，因此，通过增加每簇扇区数，可以使 FAT32 文件系统支持最大分区数。一个分区缺省的簇大小取决于该分区的大小。字段的合法十进制值有 1、2、4、8、16、32、64 和 128。Windows 2000 的 FAT32 实现只能创建最大为 32GB 的分区。但是，Windows 2000 能够访问由其他操作系统(Windows 95、OSR2 及其以后的版本)所创建的更大的分区。 |
| 0x0E     | 2              | 0x0020             | 保留扇区数(Reserved Sector) 。第一个 FAT 开始之前的扇区数，包括 DBR 引导扇区。本字段的十进制值一般为 32。 |
| 0x10     | 1              | 0x01               | FAT 数(Number of FAT) 。该分区上 FAT 的副本数。本字段的值一般为 2。 |
| 0x11     | 2              | 0x0000             | 根目录项数(Root Entries)。只有 FAT12/FAT16 使用此字段，FAT32 分区本字段必须设置为 0。 |
| 0x13     | 2              | 0x0000             | 小扇区数(Small Sector)。只有 FAT12/FAT16 使用此字段，FAT32 分区本字段必须设置为 0。 |
| 0x15     | 1              | 0xF8               | 媒体描述符( Media Descriptor)提供有关媒体被使用的信息。值 0xF8 表示硬盘，0xF0 表示高密度的 3.5 寸软盘。媒体描述符要用于 MS-DOS FAT16 磁盘，在 Windows 2000 中未被使用 |
| 0x16     | 2              | 0x0000             | 每 FAT 扇区数(Sectors Per FAT)。只被 FAT12/FAT16 所使用，FAT32 分区本字段必须设置为 0。 |
| 0x18     | 2              | 0x003F             | 每道扇区数(Sectors Per Track)。 包含使用 INT13h 的磁盘的“每道扇区数”几何结构值。该分区被多个磁头的柱面分成了多个磁道。 |
| 0x1A     | 2              | 0x00FF             | 磁头数(Number of Head) 。本字段包含使用 INT 13h 的磁盘的“磁头数”几何结构值。例如，在一张 1.44MB 3.5 英寸的软盘上。 |
| 0x1C     | 4              | 0x0000003F         | 隐藏扇区数(Hidden Sector) 该分区上引导扇区之前的扇区数。在引导序列计算到根目录的数据区的绝对位移的过程中使用了该值。本字段一般只对那些在中断 13h 上可见的媒体有意义。在没有分区的媒体上它必须为 0。 |
| 0x20     | 4              | 0x00747F71         | 总扇区数(Large Sector) 。本字段包含 FAT32 分区中总的扇区数。 |
| 0x24     | 4              | 0x000003A5         | 每 FAT 扇区数(Sectors Per FAT)，只被 FAT32 使用。该分区每个 FAT 所占的扇区数。计算机利用这个数和 FAT 数以及隐藏扇区数(本表中所描述的)来决定根目录从哪里开始。该计算机还可以从目录中的项数决定该分区的用户数据区从哪里开始。 |
| 0x28     | 2              | 0x0000             | 扩展标志(Extended Flag)，只被 FAT32 使用。该两个字节结构中各位的值为： 位 0-3：活动 FAT 数(从 0 开始计数，而不是 1)，只有在不使用镜像时才有效； 位 4-6：保留； 位 7：0 值意味着在运行时 FAT 被映射到所有的 FAT，1 值表示只有一个 FAT 是活动的； 位 8-15：保留。 |
| 0x2A     | 2              | 0x0000             | 文件系统版本(File ystem Version)，只供 FAT32 使用。高字节是主要的修订号，而低字节是次要的修订号。本字段支持将来对该 FAT32 媒体类型进行扩展。如果本字段非零，以前的 Windows 版本将不支持这样的分区。 |
| 0x2C     | 4              | 0x00000002         | 根目录簇号(Root Cluster Number)，只供 FAT32 使用。根目录第一簇的簇号。本字段的值一般为 2，但不总是如此。 |
| 0x30     | 2              | 0x0001             | 文件系统信息扇区号(File System Information SectorNumber)，只供 FAT32 使用。FAT32 分区的保留区中的文件系统信息(File System Information, FSINFO)结构的扇区号。其值一般为 1。在备份引导扇区(Backup Boot Sector)中保留了该 FSINFO 结构的一个副本，但是这个副本不保持更新。 |
| 0x34     | 2              | 0x0006             | 备份引导扇区，只供 FAT32 使用。为一个非零值，这个非零值表示该分区保存引导扇区的副本的保留区中的扇区号。本字段的值一般为 6，建议不要使用其他值。 |
| 0x36     | 12             | 12 个字节均为 0x00 | 保留。只供 FAT32 使用，供以后扩充使用的保留空间。本字段的值总为 0。 |

表 1 FAT32 分区的 BPB 字段表

拓展 BPB 参数如下：

| 字节位移 | 字段长度(字节) | 图 3 对应取值 | 字段名称和定义                                               |
| -------- | -------------- | ------------- | ------------------------------------------------------------ |
| 0x40     | 1              | 0x80          | 物理驱动器号( Physical Drive Number) ，与 BIOS 物理驱动器号有关。软盘驱动器被标识为 0x00，物理硬盘被标识为 0x80，而与物理磁盘驱动器无关。一般地，在发出一个 INT13h BIOS 调用之前设置该值，具体指定所访问的设备。只有当该设备是一个引导设备时，这个值才有意义。 |
| 0x41     | 1              | 0x00          | 保留(Reserved)。FAT32 分区总是将本字段的值设置为 0。         |
| 0x42     | 1              | 0x29          | 扩展引导标签(Extended Boot Signature)。本字段必须要有能被 Windows 2000 所识别的值 0x28 或 0x29。 |
| 0x43     | 4              | 0x00000000    | 分区序号(Volume Serial Number)。在格式化磁盘时所产生的一个随机序号，它有助于区分磁盘。 |
| 0x47     | 11             | “NO NAME”     | 卷标(Volume Label)。本字段只能使用一次，它被用来保存卷标号。现在，卷标被作为一个特殊文件保存在根目录中。 |
| 0x52     | 8              | “FAT32”       | 系统 ID(System ID)。FAT32 文件系统中一般取为”FAT32”。        |

表 2 FAT32 分区的扩展 BPB 字段

可以通过上述定义分析各个字段的含义，也可以通过 WinHex 中直接查看（逻辑分区–>右键–>模板），如图 4 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_04_FAT32_DBR_info.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_04_FAT32_DBR_info.png)

图 4 FAT32 文件系统 DBR 属性

### 2.3 文件系统信息扇区

FAT32 文件系统在 DBR 的保留扇区中安排了一个文件系统信息扇区，用以记录数据区中空闲簇的数量及下一个空闲簇的簇号，该扇区一般在分区的 1 号扇区，也就是紧跟着 DBR 后的一个扇区，其内容如图 5 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_05_FAT32_DBR_Res.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_05_FAT32_DBR_Res.png)

图 5 FAT32 文件系统信息扇区

各字段的含义如下：

-   52 52 61 41：拓展引导标签；
-   接下来 480 字节未使用，如果安装了操作系统在这个分区上的话应该是有用的；
-   72 72 41 61：文件系统信息签名；
-   0 01 D1 E9：空闲簇数，约为 3.64GB；
-   00 00 00 08：下一个空闲簇号；
-   接下来的 14 个字节：未用；
-   55 AA：结束标志；

### 2.4 FAT 表

根据 2.2 小结里面的分析，DBR 引导扇区之后会有一段保留扇区（包括 DBR 引导扇区），保留扇区数(Reserved Sector) 为 0x20（表 1 中 0x0E 字段），所以第一个 FAT 的物理扇区为：

第一个 FAT 的物理扇区 = DBR 所在位置+保留扇区数 = 0x3F + 0x20 = 0x5F

跳转到第一个 FAT 的物理扇区，如图 6 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_06_FAT32_FAT.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_06_FAT32_FAT.png)

图 6 FAT32 文件系统 FAT 表项

FAT 表项编号从 0 开始，编号 0 表示 FAT 介质类型，编号 1 表示 FAT 文件系统错误标志，这两个表项均不与实际的物理地址对应。

从 FAT 表项编号 2 开始为数据区表项，这里开始才与物理地址对应。其中，2 号表项往往是根目录(格式化就生成了)，占簇区顺序上的第 1 个簇（即 2 号簇），这也可以从表 1 中 0x2C 字段确认。

接下来，3~7 号表项为磁盘中存储的文件，共 5 个文件，每个文件都比较小，各自占用了 1 个簇。**文件至少占用一个簇，所以新建文件的时候，即使你只写入 1 字节的数据，它也会占用一个簇的空间**。如果是存储的大文件，则会占用多个簇，当前 FAT 表项纪录下一个 FAT 表项编号，依次类推直到最后以“0F FF FF FF“表示文件末尾。

### 2.5 数据区

同样，根据 2.2 小节的表格，FAT 数为 1（表 1 中 0x10 字段），所以本例中没有 FAT2，那么接下来就是数据区，先来定位数据区的物理扇区。

数据区的物理扇区 = 第一个 FAT 的物理扇区 + FAT 扇区数（表 1 中 0x24 字段） = 0x5F + 0x0000 03A5 = 0x0000 0404

跳转到数据区，如图 7 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_07_FAT32_Data.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_07_FAT32_Data.png)

图 7 FAT32 文件系统数据区

图中对应 2 号 FAT 表项，也就是根目录区。根目录区，共有 5 个文件，其中上下红框处为自定义的 2 个文件。

为了弄清楚根目录下文件各字段的含义，先看一下 FAT32 短目录项的定义，短目录项就是文件名长 8 位、后缀为 3 位的文件，更长的文件名需要长文件名，后续再说。FAT32 短文件目录项定义如下：

| 字节偏移(16 进制) | 字节数 | 定义                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| 0x0~0x7           | 8      | 文件名                                                       |
| 0x8~0xA           | 3      | 扩展名                                                       |
| 0xB*              | 1      | 属性字节： 00000000(读写) 00000001(只读) 00000010(隐藏) 00000100(系统) 00001000(卷标) 00010000(子目录) 00100000(归档) |
| 0xC               | 1      | 系统保留                                                     |
| 0xD               | 1      | 创建时间的 10 毫秒位                                         |
| 0xE~0xF           | 2      | 文件创建时间                                                 |
| 0x10~0x11         | 2      | 文件创建日期                                                 |
| 0x12~0x13         | 2      | 文件最后访问日期                                             |
| 0x14~0x15         | 2      | 文件起始簇号的高 16 位                                       |
| 0x16~0x17         | 2      | 文件的最近修改时间                                           |
| 0x18~0x19         | 2      | 文件的最近修改日期                                           |
| 0x1A~0x1B         | 2      | 文件起始簇号的低 16 位                                       |
| 0x1C~0x1F         | 4      | 表示文件的长度                                               |

表 3 FAT32 短文件目录项 32 个字节的表示定义

**因为 FAT32 使用 4 个字节表示文件或目录大小，因此当文件或目录大于 4Gb 时将会溢出，做截断处理。**

FAT32 文件系统分区根目录的文件和目录都存放在根目录区中，子目录文件和文件夹存放在子目录区中，以 32 字节为一项存放目录项（FDT）。

结合图 7 中 0x000808C0~0x000808DF 地址，对照表 3 解释一下各字段的含义：

（1）目录项 0x00~0x07 为文件名“123”，0x08~0x0A 为扩展名“txt”，0x0B 处值为 20，表示的是文件。

（2）目录项 0x0E~0x0F 为文件创建时间：0x5E75 = 0b 0101 1110 0111 0101 –> 01011(11) 110011(51) 10101(21*2) = 11:51:42，即 11 点 51 分 42 秒。

（3）目录项 0x10~0x11 为文件创建日期：0x528C = 0b 0101 0010 1000 1100 –> 0101001(41+1980=2021) 0100(4) 01100(12)，即 2021 年 4 月 12 日。

（4）文件起始簇号：0x14~0x15，文件起始簇号的高 16 位；0x1A~0x1B，文件起始簇号的低 16 位，即 0x0000 0007，和 FAT 表项中的占用一致。

（5）文件大小：0x1C~0x1F，即 0x0000 000A，占用 10 字节。

现在打开文件属性看一下，如图 8 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_08_FAT32_123_txt.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_08_FAT32_123_txt.png)

图 8 123.txt 文件属性

可以看出和分析的一致，占用空间为 32KB，因为该文件占用一簇，一簇有 64 扇区，每个扇区 512 字节，共 32KB。

接下来看到第 7 簇看一下该文件的内容，如图 9 所示。

[![img](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_09_FAT32_123_txt_content.png)](https://www.sunev.cn/blog/wp-content/uploads/2021/04/20210408_09_FAT32_123_txt_content.png)图 9 123.txt 文件内容对比

也和实际的 123.txt 文件内容一致。

根据上面的分析，抽茧剥丝，从 MBR 到 DBR，再到 FAT，再到目录区，最后找到文件的存储区域，弄清楚了 FAT32 文件系统的结构，后续将结合几个具体的文件操作来进一步理解 FAT32 文件系统。

## 三、NAND FLASH Memory Map

![image-20210919165557745](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20210919165557745.png)

![image-20210919170805368](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20210919170805368.png)

RA[17:6]表示Blocks的index，RA[5:0]表示Pages的index，CA[11:0]表示具体到每个page中字节的地址。

RA[17:6]有12位，最大为2^12=4096，说明Blocks只有4096个，index范围为[0:4095]。

RA[5:0]有6位，最大为2^6=64，表示每个block有64个page。

CA[11:0]有12位，但是实际只有2175Byte可用。

每次操作时最小单元就是page，则最小单元扇区为：page_size=4096Byte，实际只有2175Byte，可用的为2048Byte=2KByte。

每个block有64 page，故block size=page_num*page_size=64\*4096Byte=256KByte，实际可用为128Kbyte。

sector：表示扇区，每个扇区有1page，sector size：2KByte。sector可等同于page。

cluster：表示簇，每个簇有64page或者64sector，cluster size:128Kbyte。cluster可等同于block。

总计有4096*64个page。



int8_t STORAGE_GetCapacity_FS(uint8_t lun, uint32_t *block_num, uint16_t *block_size)

这里的block_num指的是扇区的个数，即page的个数，为64*4096；block_size指的是一个扇区大小，即page大小，为2048Byte，即2KByte。



int8_t STORAGE_Read_FS(uint8_t lun, uint8_t *buf, uint32_t blk_addr, uint16_t blk_len)

int8_t STORAGE_Write_FS(uint8_t lun, uint8_t *buf, uint32_t blk_addr, uint16_t blk_len)

传进来的参数是扇区的地址和扇区的个数（即page的index和page个数），在进行读的时候要转换成字节地址和字节大小，读写是按照page来操作的。但是写之前需要擦除block，写block中，剩余page时不需要重复擦写。



写函数先将1 block内容读出来，再擦除，然后写进去。page是否为脏污应该由fat表来表明，但首先应该先擦除全部空间。读写速度受到限制。



使用数组flag标记是否脏污，或者擦除过。但是这种，脏污后重新擦除时不可用，因为标记是说明是否有擦除。如果有写过则是脏page，再写时需要擦除。如果不擦除则无法写入。每次断电后参数复位后，可能会重新擦除。这时候是由FAT表和FATFS管理。断电后写重复位置会擦除该区域。



```c

/**
  * @brief  传进来的参数是扇区的地址和扇区的个数（即page的地址和page个数），在进行读的时候要转换成字节地址和字节大小
  * 这里USB的最大数据包是2048，为1page，故blk_len最大就是1
  * @param  lun: .
  * @retval USBD_OK if all operations are OK else USBD_FAIL
  */
int8_t STORAGE_Read_FS(uint8_t lun, uint8_t *buf, uint32_t blk_addr, uint16_t blk_len)
{
  /* USER CODE BEGIN 6 */
  uint32_t n;
  uint32_t block_num = 0;
  uint32_t page_num = 0;

  if (blk_len > 1)
  {
    return USBD_FAIL;
  }
  //SEGGER_RTT_printf(0, "Read=> blk_addr=%d,     blk_len=%d\r\n", blk_addr, blk_len);
  block_num = blk_addr / 64;
  page_num = blk_addr % 64;
  flash_Read(block_num, page_num, 0, buf, STORAGE_BLK_SIZ);
  //SEGGER_RTT_printf(0, "Read=> Block=%d,Page=%d\r\n", block_num, page_num);
  return (USBD_OK);
  /* USER CODE END 6 */
}
uint8_t erase_flag[512] = {0}; //block erase flag,0:not erase,1:erase
uint8_t erase_f = 0x00;
uint8_t data_buf_t[2048];
uint32_t temp_block_num = 5000;

/**
  * @brief  .
  * @param  lun: .
  * @retval USBD_OK if all operations are OK else USBD_FAIL
  */
int8_t STORAGE_Write_FS(uint8_t lun, uint8_t *buf, uint32_t blk_addr, uint16_t blk_len)
{
  /* USER CODE BEGIN 7 */
  uint32_t n;
  uint32_t block_num = 0;
  uint32_t page_num = 0;
  SEGGER_RTT_printf(0, "Write=> blk_addr=%d,     blk_len=%d\r\n", blk_addr, blk_len);

  block_num = blk_addr / 64;
  page_num = blk_addr % 64;
  if ((erase_flag[block_num / 8] & erase_f) == 0)
  {
    /*
    flash_Erase(4095);
    for (n = 0; n < 64; n++)
    {
      flash_Read(block_num, n, 0, data_buf_t, STORAGE_BLK_SIZ);
      flash_Write(4095, n, 0, data_buf_t, STORAGE_BLK_SIZ);
    }
    */
    flash_Erase(block_num);

    erase_f = (1 << (block_num % 8));
    erase_flag[block_num / 8] |= erase_f;
    SEGGER_RTT_printf(0, "Write=> Erase Block=%d\r\n", block_num);
  }

  flash_Write(block_num, page_num, 0, buf, STORAGE_BLK_SIZ);
  /*
  if (temp_block_num != block_num)
  {
    for (n = 0; n < page_num; n++)
    {
      flash_Read(4095, n, 0, data_buf_t, STORAGE_BLK_SIZ);
      flash_Write(block_num, n, 0, data_buf_t, STORAGE_BLK_SIZ);
    }
    for (n = page_num; n < 64; n++)
    {
      flash_Read(4095, n, 0, data_buf_t, STORAGE_BLK_SIZ);
      flash_Write(block_num, n, 0, data_buf_t, STORAGE_BLK_SIZ);
    }
  }
  temp_block_num = block_num;
  */
  return (USBD_OK);
  /* USER CODE END 7 */
}
```



后续的读写如果考虑erase就擦除，可能导致写不进去。需要擦除后再写。

```c
/*---------- -----------*/
#define USBD_MAX_NUM_INTERFACES     1U
/*---------- -----------*/
#define USBD_MAX_NUM_CONFIGURATION     1U
/*---------- -----------*/
#define USBD_MAX_STR_DESC_SIZ     2048U
/*---------- -----------*/
#define USBD_DEBUG_LEVEL     0U
/*---------- -----------*/
#define USBD_LPM_ENABLED     1U
/*---------- -----------*/
#define USBD_SELF_POWERED     1U
/*---------- -----------*/
#define MSC_MEDIA_PACKET     2048U

/* MSC Class Config */
#ifndef MSC_MEDIA_PACKET
#define MSC_MEDIA_PACKET             512U
#endif /* MSC_MEDIA_PACKET */

#define MSC_MAX_FS_PACKET            0x40U
#define MSC_MAX_HS_PACKET            0x200U

#define BOT_GET_MAX_LUN              0xFE
#define BOT_RESET                    0xFF
#define USB_MSC_CONFIG_DESC_SIZ      32


#define MSC_EPIN_ADDR                0x81U
#define MSC_EPOUT_ADDR               0x01U
```

可见USB操作时最大是2048Byte，即2Kbyte。就是1page数据。



Fatfs和USB都是按照最小单元page（sector）进行读写。即每次都是读写1page数据。



挂载和open有问题，貌似没有FAT表。写是128K擦除，读是2K读，导致读写page时如果写的是同一个block的同一个page则需要擦除整个block，会导致其他数据丢失。

改成以下方式后，erase次数太多，但是调试OK。

```c
uint8_t data_buf_t[2048];
uint32_t temp_block_num = 5000, temp_page_num = 65;
DRESULT USER_write(
    BYTE pdrv,        /* Physical drive nmuber to identify the drive */
    const BYTE *buff, /* Data to be written */
    DWORD sector,     /* Sector address in LBA */
    UINT count        /* Number of sectors to write */
)
{
  /* USER CODE BEGIN WRITE */
  /* USER CODE HERE */
  uint32_t n = 0, k = 0;
  uint32_t block_num = 0;
  uint32_t page_num = 0;
  uint8_t i = 0, j = 0, temp = 0;

  SEGGER_RTT_printf(0, "Fatfs Write=> sector=%d,     count=%d\r\n", sector, count);

  for (n = 0; n < count; n++)
  {
    block_num = sector / 64;
    page_num = sector % 64;

    flash_Erase(BLOCK_RSV);
    for (k = 0; k < 64; k++)
    {
      flash_Read(block_num, k, 0, data_buf_t, PAGE_SIZE);
      flash_Write(BLOCK_RSV, k, 0, data_buf_t, PAGE_SIZE);
    }
    flash_Erase(block_num);
    SEGGER_RTT_printf(0, "Fatfs Erase=> block=%d\r\n", block_num);

    for (i = 0; i < 64; i++)
    {
      if (i == page_num)
      {
        flash_Write(block_num, i, 0, (uint8_t *)&buff[0 + n * PAGE_SIZE], PAGE_SIZE);
      }
      else
      {
        flash_Read(BLOCK_RSV, i, 0, data_buf_t, PAGE_SIZE);
        flash_Write(block_num, i, 0, data_buf_t, PAGE_SIZE);
      }
    }

    sector++;
    //SEGGER_RTT_printf(0, "Write=> Block=%d,Page=%d\r\n", block_num, page_num);
  }
  return RES_OK;
  /* USER CODE END WRITE */
}
```



写时如果不close，则无法同时read。
