* [项目介绍](项目介绍)
* [前期准备](前期准备)
* [常用命令介绍](常用命令介绍)
* [开发流程](开发流程)
* [注意事项](注意事项)

项目介绍
---
##### 这是一个使用python框架scrapy实现爬虫的项目，爬取站点是[预告片世界](http://www.yugaopian.cn/allmovies),将抓取的item保存在json文件中，同时下载图片  
##### scrapy框架是python下一款轻量级web爬虫框架，主要用于数据挖掘、监测和自动化测试。Scrapy吸引人的地方在于它是一个框架，任何人都可以根据需求方便的修改。它也提供了多种类型爬虫的基类，如BaseSpider、sitemap爬虫等，最新版本又提供了web2.0爬虫的支持。

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
 常用命令介绍
 ---
 scrapy安装成功后，就可以通过scrapy命令来创建和开发项目，首先来认识一下scrapy的命令： 
 * scrapy startproject app --创建名字为app的项目
 * scrapy genspider aiqiyi 'aiqiyi.com' --创建名为aiqiyi的爬虫，允许爬取的域名是aiqiyi.com
 * scrapy crawl aiqiyi [-o aiqiyi.json] --运行名为aiqiyi的爬虫，中括号中为直接生成json文件，可选
 * scrapy list  --列出项目中所有的爬虫
 * scrapy shell 'http://www.aiqiyi.com' --以shell控制台的形式进行调试，方便获取提取规则
 * scrapy runspider aiqiyi  --直接运行aiqiyi爬虫，不运行项目
 * scrapy --help ---查看scrapy命令
 * scrapy version ---查看版本信息  
 基本上这些命令足够完成爬虫的开发了 
 
开发流程
 ---
 1. 在电脑中选择一个用于开发爬虫的目录，比如D:aiqiyi,可以通过命令行创建
 ```
 C:\Users\admin>d:

D:\>mkdir aiqiyi
```
创建完成后，直接cd到该目录中。  
2. 运行scrapy命令创建项目，命令如下：
```
scrapy startproject aiqiyi
```
3. 打开开发工具，可以使用sublime，当然最专业的就是pycharm了。使用pycharm导入刚刚创建的项目，导入成功后就可以看到这样的文档结构：
```
aiqiyi
  aiqiyi
    __pycache__
    spiders           # 爬虫目录，所有编写的爬虫文件都在这个目录中
       __pycache__
      __init__.py     # init文件，代表这是一个包，而不是一个简简单单的目录
    __init__.py
    items.py          # 定义爬取item的字段，所有字段类型类似字典
    middlewares.py    # 中间件文件，一般用的不多
    pipelines.py      # 管道文件，处理爬取结果
    settings.py       # 配置文件,相当重要，管道文件开启、指定图片下载目录都在这个文件里设置
  scrapy.cfg
  ```
  4. 切换到pycharm的Terminal控制台，运行命令创建第一个爬虫文件，命令如下：
  ```
  scrapy genspider aiqiyispider 'aiqiyi.com'
  ```
  过一会就会在刚才的spider目录中看到aiqiyispider.py文件，所有爬取的逻辑和提取文件的规则都写在这里面。  
  5. 打开aiqiyispider.py文件，要注意几个重要的属性：
  ```
  class aiqiyispiderSpider(scrapy.Spider):
    name = 'aiqiyispider'                                   # name是爬虫项目唯一的标识，同一个项目中一定不要使用同一个name
    allowed_domains = ['www.yugaopian.cn']                  # 这个可选
    start_urls = ['http://www.yugaopian.cn/allmovies']      # 爬虫启动时第一个爬取的网址，这里可以用列表，也可以用元组，元组注意加逗号
    
    def parse(self, response):                              # 爬虫默认的解析方法，方法名不能变
      movlist = response.xpath("//div[@class='movlist']/ul/li")    # 从这里开始，都是提取item的规则，使用xpath语法
        for result in movlist:
            item = YugaopianItem()
            item['name'] = result.xpath("./a/span[@class='item-title']/text()")[0].extract()
            item['pub_date'] = result.xpath("./a/span[@class='item-pubtime']/text()")[0].extract()
            item['movie_cover'] = result.xpath("./a/img/@src").extract()
            item['url'] = "%s%s" % ("https://www.yugaopian.cn", result.xpath("./a/@href")[0].extract())
            item['img_urls'] = item['movie_cover']
            
            # 获取详情页URL，通过使用options方式将item传递
            request = scrapy.Request(url=item['url'], meta={"key": item}, callback=self.parse_detail)
            
            # 这里yield的使用非常重要，等待下一次请求到来，将本次请求发出去
            yield request
            
            # 给爬虫设置条件，如果是最后一页，就终止
            if response.xpath("//p[@class='page-nav']/a[text()='下一页']/@href"):
                next_url = "%s%s" % (
                    "https://www.yugaopian.cn",
                    response.xpath("//p[@class='page-nav']/a[text()='下一页']/@href")[0].extract())
                yield scrapy.Request(next_url, callback=self.parse)
      #pass
    def parse_detail(self, response):
        item = response.meta['key']
        #   // div[ @class ='movie-title-detail'] / p / span[@ class ="detail-title" and text()="导演："] / following-sibling:: a[1] / text()
        item['director'] = response.xpath(
            '//div[@class="movie-title-detail"]/p/span[@class="detail-title" and text()="导演："]/following-sibling::a[1]/text()')[0].extract()
        item['actor'] = response.xpath(
            '//div[@class="movie-title-detail"]/p/span[@class="detail-title" and text()="主演："]/following-sibling::a/text()')[0].extract()
        item['desc'] = response.xpath(
            '//div[@class="movie-title-detail"]/p/span[@class="detail-title" and text()="剧情："]/following-sibling::text()')[0].extract()
        yield item
   ```
  

 

 
 





