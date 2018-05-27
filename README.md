* [项目介绍](项目介绍)
* [前期准备](前期准备)
* [开发流程](开发流程)
* [注意事项](注意事项)

项目介绍
---
##### 这是一个使用python框架scrapy实现爬虫的项目，爬取站点是[预告片世界](http://www.yugaopian.cn/allmovies),将抓取的item保存在json文件中，同时下载图片  
#### scrapy框架是python下一款轻量级web爬虫框架，主要用于数据挖掘、监测和自动化测试。Scrapy吸引人的地方在于它是一个框架，任何人都可以根据需求方便的修改。它也提供了多种类型爬虫的基类，如BaseSpider、sitemap爬虫等，最新版本又提供了web2.0爬虫的支持。

前期准备
---
* python下载和安装  
1. python下载。目前python有python2和python3两个版本，两个版本之间有很大差异，如果现在要用python开发，那选择python2，而如果只是想学习python这门语言的话，首选python3，因为python3是未来的首选版本。这个项目采用的python3.6。[下载地址](https://www.python.org/downloads/)
2. python安装。python下载完成后，直接按照提示进行安装，安装完成后，在cmd控制台直接输入python命令，如果显示版本号则表示安装成功。如下：
```
python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
* scrapy下载与安装  
python安装成功后，就可以直接通过pip install xx来安装所需模块（xx是模块名），但scarpy算是一个比较大的模块框架，你直接用pip install scrapy会显示安装失败，不信你可以试试。因此要采用特殊的方法，下面是摸(cai)索(keng)的过程:  
1、下载scrapy的whl包,[下载地址](http://www.lfd.uci.edu/~gohlke/pythonlibs/),打开网址后，在网页中搜索scrapy，然后找到Scrapy‑1.5.0‑py2.py3‑none‑any.whl，下载了scrapy的whl包先不要着急安装  
2、 安装whl格式包需要安装wheel库，可以直接使用pip install wheel安装wheel。  
3、 scrapy依赖twisted，同样使用whl格式的包进行安装，还是进入[下载地址](http://www.lfd.uci.edu/~gohlke/pythonlibs/),，在网页中搜索twisted找到其对应的whl包Twisted‑18.4.0‑cp36‑cp36m‑win_amd64.whl并下载,根据你的Python的版本选择合适的包，名称中间的cp36是python3.6的意思，amd64是python的位数。  
4、 下载完成后使用cmd打开windows的命令行窗口，进入whl包所在的文件夹执行如下命令：pip install [whl]，[whl]是whl包的名字，即：
  ```
  pip install Twisted-17.1.0-cp36-cp36m-win_amd64.whl  
  ```  
  Scrapy包需要其所有依赖的包安装完成后才能进行安装，现在还不能安装  
  5、 scrapy依赖lxml包，需要先安装lxml包，lxml包依赖libxml2，libxml2-devel，所以安装lxmllibxml2， libxml2-devel。幸运的是之前我之前已经安装过lxml   
  6、所有准备工作做完，中医可以安装scrapy包了，进入Scrapy-1.3.3-py2.py3-none-any.whl所在的目录  
  ```
  pip install Scrapy-1.3.3-py2.py3-none-any.whl  
  ```
  7、 Successfully ! 先别急着撒花，是否真的安装成功了，还需要验证，输入scrapy -h，出现以下显示，恭喜你安装成功了：
  ```
  C:\Users\Administrator>scrapy -h
  Scrapy 1.5.0 - no active project

  Usage:
    scrapy <command> [options] [args]

  Available commands:
    bench         Run quick benchmark test
    fetch         Fetch a URL using the Scrapy downloader
    genspider     Generate new spider using pre-defined templates
    runspider     Run a self-contained spider (without creating a project)
    settings      Get settings values
    shell         Interactive scraping console
    startproject  Create new project
    version       Print Scrapy version
    view          Open URL in browser, as seen by Scrapy

    [ more ]      More commands available when run from project directory

  Use "scrapy <command> -h" to see more info about a command
  ```





