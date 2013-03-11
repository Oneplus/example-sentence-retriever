例句查找小助手
=============

![很难看的截图](https://raw.github.com/Oneplus/example-sentence-retriever/master/assets/figure.png)

这是一个用来帮助标注者标注数据的一个小工具。在标注者拿不准某些句子片段应该如何划分或者如何标词性时，这个小助手可以提供一定的参考。

### 配置

例句文件放在corpus这里，暂时是gbk编码的。

例句文件的格式可以参考项目中的sample，很简单的。

### 开发

依赖以下一些模块

* pyqt4
* py2exe

界面是用qt designer画的。

### 编译出可执行程序

```
python setup.py py2exe --includes sip
```

### 附注

名字很土 :(
