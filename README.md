# CMS-Django3.x-StaticWhiteWeb
CMS Django3.x 开发环境前后端分离，xadmin后端管理，白色前端静态模板。

项目整体介绍地址 [『Python-Django 智慧中医健康数字服务平台』开源项目总览](https://datayang.blog.csdn.net/article/details/122918137)

# 项目开发初衷
本人2018年-2020年曾就职于清华大学天津高端装备研究院下属的智慧医疗与医药装备研究所，并开始接触中医相关方向的内容，由于诸多的原因最初是带有一些抵触的情绪，后来一些机缘巧合让我迷恋上了中医，看着市面上形形色色的互联网中医产品，无尽的感慨也想拥有一套自己的这样的内容的产品。

由于本人多少有些强迫症和完美主义的情感因素的影响，再加上自己掌握一些简单的技术，所以想着利用技术结合现在互联网以及书籍上能看到的所有信息进行综合的采集管理，给后辈的小伙伴一个综合参考的案例，内容会不断的更新在这个帖子中，欢迎收藏和保留。

**项目演示地址：[Mr数据杨的CMS管理平台](https://cms.datayang.cn)**

由于本人开发的项目比较多并且服务器资源有限，因此会有先择性的开发部分系统进行展示，如果网页打不开私信联系我进行项目启动。

**我的个人介绍和全部项目展示地址：[Mr数据杨的个人主页](https://home.datayang.cn)**


# 项目技术应用
本项目基于Python语言开发，内容主要涵盖以下几方面内容：

 **数据采集模块**
 
 1. **Scrapy爬虫框架** 分布式采集CMS平台需要的内容数据信息；![在这里插入图片描述](https://img-blog.csdnimg.cn/d65f3c9d771d46899b238bc270e0c34f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXLmlbDmja7mnag=,size_20,color_FFFFFF,t_70,g_se,x_16)
2. **Gerapy爬虫管理框架** 进行爬虫脚本的部署任务的管理；
![在这里插入图片描述](https://img-blog.csdnimg.cn/6a019982979b4aefb4b09039a5388a05.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXLmlbDmja7mnag=,size_20,color_FFFFFF,t_70,g_se,x_16)

**数据处理模块**

 1. 实现 **pandas** 、**pymysql** 、**pymongo** 等对抓取的数据进行处理，整合成 **Django框架** 中API接口需要的形式；
![在这里插入图片描述](https://img-blog.csdnimg.cn/7334c21ccf964047a691506dd9ec6a1c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXLmlbDmja7mnag=,size_20,color_FFFFFF,t_70,g_se,x_16)
 2. 基于 **深度学习** 中 **卷积神经网络（CNN）** 和 **循环神经网络（RNN）** 设计的文本多分类模型；
![在这里插入图片描述](https://img-blog.csdnimg.cn/5f3e248661b545e595be47ba6c7c6011.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXLmlbDmja7mnag=,size_20,color_FFFFFF,t_70,g_se,x_16)

**数据分析模块**

 1. 用基础的站点数据统计进行简单的访问数据分析；
![在这里插入图片描述](https://img-blog.csdnimg.cn/5ce95aa7bc8b481abf529df6e51f1ce8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXLmlbDmja7mnag=,size_20,color_FFFFFF,t_70,g_se,x_16)

**数据产品**

 1. 基于  **moviepy框架** 进行结合文本转视频的自媒体的内容，github参考地址：[Moviepy图文一键转视频-V1.0
](https://github.com/Escaflowne1985/ArticleGenerationVideo-V1.0)，内容待整理后放出。
![在这里插入图片描述](https://img-blog.csdnimg.cn/da018d7ddd4c492eb3238bbf67925714.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXLmlbDmja7mnag=,size_20,color_FFFFFF,t_70,g_se,x_16)![在这里插入图片描述](https://img-blog.csdnimg.cn/c7f7b204b8e946969dbdb039e6ddd3ae.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXLmlbDmja7mnag=,size_20,color_FFFFFF,t_70,g_se,x_16)
 2. 基于 **django REST framework** 开发的数据API接口服务，暂未想好产品逻辑；


**系统开发模块**

 1.  基于 **Django 3.x web框架** 进行系统前后端分离系统开发内容；



目前使用的以上的内容，未来随着业务的更新进行添加更新，未来打算用20年的时间在这条道路上钻研下去，未来这条路任重而道远。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210427202334256.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIwMjg4MzI3,size_16,color_FFFFFF,t_70)
# 中医科研成就

**英国科学在线发表中医问诊论文**

《Application research on quantitative prediction of traditional   Chinese medicine syndrome differentiation based on Ensemble Learning》（基于集成学习的中医问诊辨证预测应用研究）

> 检索地址：https://www.inderscienceonline.com/action/doSearch?ContribAuthorRaw=Liang%2C+Huaixin
DoI:10.1504/IJCAT.2020.111087
原文索引信息：Jan 2020, Vol. 64（卷号）, Issue 1（期号）,46-56页

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210402103852516.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIwMjg4MzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210402104029579.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIwMjg4MzI3,size_16,color_FFFFFF,t_70)
# 项目更新历程

**本着对付费用户负责的原则，本栏目长期更新，所有历史文章全部保留**

**V1.0 更新目录**

在2020年10月19日完成了第一版的开发工作以及对应文字教程。对应版本内容搜索专栏下的标题，1.0版权已经卖出。

版本名称：**『基于Python技术的智慧中医商业项目』**

 - 2020.01.05 Gerapy数据采集管理系统
 - 2020.10.05 完成数据后台API
 - 2020.10.12 完成Web前端
 - 2020.10.19 完成中医问诊系统

**V2.0 更新目录**

从2021年的2月新年伊始准备了第二版的内容，目前也已经完成变化内容较大，已经和V1.0版本完全是不同的内容了。很多1.0版本中未更新的内容均会在2.0版本中进行更新。请对应版本内容搜索专栏下的标题。

版本名称：**『Python-Django 智慧中医健康数字服务平台』**

- 2021.02.11 暂时下架中医问诊系统
- 2021.02.12 重写数据后台API接口
- 2021.02.14 重写Web前端 
- 2021.02.16 增加前后端交互API 
- 2021.02.17 增加用户功能后台功能


**V3.0 更新目录**

目前项目进入3.0版本，填前面的所有坑以及更新拓展的内容。

# 专栏文章索引
**项目整体介绍**

- [『Python 自制CMS开源系统』智慧中医健康数字服务平台](https://blog.csdn.net/qq_20288327/article/details/109242573)

**中医学习笔记**

- [「Python-Django 智慧中医健康数字服务平台」中医问诊学习，开发原理理论基础](https://blog.csdn.net/qq_20288327/article/details/109443658)

**数据管理模块**

- [「Python3 爬虫标准化项目」环境搭建与爬虫框架Scrapy入门](https://blog.csdn.net/qq_20288327/article/details/113623896)
- [「Python3 爬虫标准化项目」爬虫目标整理和数据准备](https://blog.csdn.net/qq_20288327/article/details/113626985)
- [「Python3 爬虫标准化项目」标准化爬虫数据抓取通用代码编写模板](https://blog.csdn.net/qq_20288327/article/details/113643944)
- [「基于Django的智慧中医数字服务商业项目」Scrapy数据采集模板样例](https://blog.csdn.net/qq_20288327/article/details/109046682)
- [「基于Django的智慧中医数字服务商业项目」数据采集篇爬虫管理](https://blog.csdn.net/qq_20288327/article/details/109031861)
- [「基于Django的智慧中医数字服务商业项目」数据NLP的数据处理](https://blog.csdn.net/qq_20288327/article/details/109050297)

**4.算法模型应用**

[「基于Django的全民健康智慧中医数字服务平台」基于深度学习抓取文章自动多分类算法模型](https://blog.csdn.net/qq_20288327/article/details/120328505)

**V1.0 项目介绍**

- [「基于Python技术的智慧中医商业项目」 产品思路&技术应用](https://blog.csdn.net/qq_20288327/article/details/109018242)
- [「基于Python技术的智慧中医商业项目」资讯数据&平台业务设计](https://blog.csdn.net/qq_20288327/article/details/109771981)
- [「基于Python技术的智慧中医商业项目」基于机器学习的Django问诊系统展示](https://blog.csdn.net/qq_20288327/article/details/109386120)
- [「基于Python技术的智慧中医商业项目」基于Django的Web前端页面展示](https://blog.csdn.net/qq_20288327/article/details/109265617)
- [「基于Python技术的智慧中医商业项目」基于Django的Manage管理后台展示](https://blog.csdn.net/qq_20288327/article/details/109241969)
- [「基于Python技术的智慧中医商业项目」Django后端系统配置](https://blog.csdn.net/qq_20288327/article/details/109050538)
- [「基于Python技术的智慧中医商业项目」Django后端新闻资讯应用设计](https://blog.csdn.net/qq_20288327/article/details/109053069)
- [「基于Python技术的智慧中医商业项目」Django后端用户应用设计](https://blog.csdn.net/qq_20288327/article/details/109067872)
- [「基于Python技术的智慧中医商业项目」Django后端主页应用设计](https://blog.csdn.net/qq_20288327/article/details/109160755)
- [「基于Python技术的智慧中医商业项目」Django后端知识库应用设计](https://blog.csdn.net/qq_20288327/article/details/109159219)
- [「基于Python技术的智慧中医商业项目」Django前端系统配置](https://blog.csdn.net/qq_20288327/article/details/109163290)
- [「基于Python技术的智慧中医商业项目」Django前端HTML设计](https://blog.csdn.net/qq_20288327/article/details/109237261)
- [「基于Python技术的智慧中医商业项目」Django前端用户交互设计](https://blog.csdn.net/qq_20288327/article/details/109238327)
- [「基于Python技术的智慧中医商业项目」Django前端主页数据交互](https://blog.csdn.net/qq_20288327/article/details/109239025)
- [「基于Python技术的智慧中医商业项目」Django前端资讯数据交互](https://blog.csdn.net/qq_20288327/article/details/109236727)
- [「基于Python技术的智慧中医商业项目」问诊模块系统配置](https://blog.csdn.net/qq_20288327/article/details/109384163)
- [「基于Python技术的智慧中医商业项目」问诊模块用户管理](https://blog.csdn.net/qq_20288327/article/details/109384244)
- [「基于Python技术的智慧中医商业项目」问诊模块问诊应用](https://blog.csdn.net/qq_20288327/article/details/109384425)
- [「基于Python技术的智慧中医商业项目」问诊模块后台管理](https://blog.csdn.net/qq_20288327/article/details/109385144)
- [「基于Python技术的智慧中医商业项目」问诊模块前端设计](https://blog.csdn.net/qq_20288327/article/details/109385316)

**V2.0 项目介绍**

- [「基于Django的全民健康智慧中医数字服务平台」产品设计&技术应用](https://blog.csdn.net/qq_20288327/article/details/115394523)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用系统配置](https://blog.csdn.net/qq_20288327/article/details/115349618)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用系统配置](https://blog.csdn.net/qq_20288327/article/details/115349114)
- [「基于Django的全民健康智慧中医数字服务平台」Web服务HTML代码编写规范](https://blog.csdn.net/qq_20288327/article/details/115351490)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用API接口功能（一）](https://blog.csdn.net/qq_20288327/article/details/115352520)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用API接口功能（二）](https://blog.csdn.net/qq_20288327/article/details/115352818)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用API接口功能（三）](https://blog.csdn.net/qq_20288327/article/details/115353100)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用API接口功能（四）](https://blog.csdn.net/qq_20288327/article/details/115353209)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用API接口功能（五）](https://blog.csdn.net/qq_20288327/article/details/115353384)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Articles设计思路](https://blog.csdn.net/qq_20288327/article/details/115305599)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用Articles设计思路](https://blog.csdn.net/qq_20288327/article/details/115375352)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Articles代码实现（一）](https://blog.csdn.net/qq_20288327/article/details/115323127)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Articles代码实现（二）](https://blog.csdn.net/qq_20288327/article/details/115323425)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Articles代码实现（三）](https://blog.csdn.net/qq_20288327/article/details/115323595)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Articles代码实现（四）](https://blog.csdn.net/qq_20288327/article/details/115323689)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Articles可视化](https://blog.csdn.net/qq_20288327/article/details/115323900)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用Articles功能（一）](https://blog.csdn.net/qq_20288327/article/details/115376020)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用Articles功能（二）](https://blog.csdn.net/qq_20288327/article/details/115376251)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用Articles功能（三）](https://blog.csdn.net/qq_20288327/article/details/115376601)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用Users设计思路](https://blog.csdn.net/qq_20288327/article/details/115352449)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（一）](https://blog.csdn.net/qq_20288327/article/details/115372315)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（二）](https://blog.csdn.net/qq_20288327/article/details/115372684)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（三）](https://blog.csdn.net/qq_20288327/article/details/115372761)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（四）](https://blog.csdn.net/qq_20288327/article/details/115372823)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（五）](https://blog.csdn.net/qq_20288327/article/details/115373423)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（六）](https://blog.csdn.net/qq_20288327/article/details/115373318)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（七）](https://blog.csdn.net/qq_20288327/article/details/115373423)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（八）](https://blog.csdn.net/qq_20288327/article/details/115373629)
- [「基于Django的全民健康智慧中医数字服务平台」前端应用User功能（九）](https://blog.csdn.net/qq_20288327/article/details/115374013)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Users设计思路](https://blog.csdn.net/qq_20288327/article/details/115327903)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Users代码实现（一）](https://blog.csdn.net/qq_20288327/article/details/115328896)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Users代码实现（二）](https://blog.csdn.net/qq_20288327/article/details/115329174)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Users代码实现（三）](https://blog.csdn.net/qq_20288327/article/details/115329337)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Users代码实现（四）](https://blog.csdn.net/qq_20288327/article/details/115329413)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用Users可视化](https://blog.csdn.net/qq_20288327/article/details/115329722)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用General_Data设计思路](https://blog.csdn.net/qq_20288327/article/details/115345231)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用General_Data代码实现（一）](https://blog.csdn.net/qq_20288327/article/details/115345885)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用General_Data代码实现（二）](https://blog.csdn.net/qq_20288327/article/details/115346083)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用General_Data代码实现（三）](https://blog.csdn.net/qq_20288327/article/details/115346110)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用General_Data代码实现（四）](https://blog.csdn.net/qq_20288327/article/details/115346132)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用General_Data可视化](https://blog.csdn.net/qq_20288327/article/details/115346154)
- [「基于Django的全民健康智慧中医数字服务平台」后端应用My_Home设计思路及展示](https://blog.csdn.net/qq_20288327/article/details/115348637)



# UGC自媒体
待更新

# 数据化管理运营
待更新

# 问题汇总
[【Django】开发遇见问题汇总和解决办法](https://blog.csdn.net/qq_20288327/article/details/109265593)

如果你对我做的中医数字平台感兴趣欢迎留言讨论，如果内容对你有帮助的话，能够请我喝一杯沪上阿姨不禁万分感谢。
