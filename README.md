# SoftwareAlgrithm
for a final work of 软件技术进展 course
软件技术进展
姓名：钟悦东    学号：20340081
GitHub 仓库地址:
题目：复原ip地址
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
目录
题目：复原ip地址	1
一、	敲定初步思路	1
二、	尝试实现	2
三、	Bug探查阶段	4
四、	整体测试阶段	5
五、	总结	5


一、	敲定初步思路
点分十进制地址，有限制条件
	最多不超过12个数字
	同时只需用3个点分割为四段
于是有下列结构
 

二、	尝试实现
为各个分段添加条件
	每个分段若是前导为0，那么最多只有一个数字
	同时每个分段大小不超过255
结果发现有个简单bug
	点和点之间无间隔，易解决，循环位置range起点都在+1使得点与点间的分段最小为1
 

解决后
  
三、	Bug探查阶段
首先发现为对第四段做出约束，然后在第三层循环中添加对第四段的约束。
 
Bug:”0000”这种情况无法通过
发现是红黄位置未对齐，对齐后这个bug即可修复
 

四、	整体测试阶段
在leetcode题库中测试
 
 
Debug后
 

五、	总结
这道题难度不大，整体可以暴力破解，但是三层循环硬编码中会遇到许多细节问题，需要细细推敲，当然还可以采用回溯法，那是基于分段处理的思想，我做法还是基于画点，因为纯粹循环无需函数压栈，整体效率还是非常高的。
