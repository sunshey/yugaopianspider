* [项目介绍](项目介绍)
* [前期准备](前期准备)
* [常用命令介绍](常用命令介绍)
* [开发流程](开发流程)
* [注意事项](注意事项)
* [写在最后](写在最后)

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

1. 下载scrapy的whl包,[下载地址](http://www.lfd.uci.edu/~gohlke/pythonlibs/),打开网址后，在网页中搜索scrapy，然后找到Scrapy‑1.5.0‑py2.py3‑none‑any.whl，下载了scrapy的whl包先不要着急安装  

2. 安装whl格式包需要安装wheel库，可以直接使用pip install wheel安装wheel。  

3. scrapy依赖twisted，同样使用whl格式的包进行安装，还是进入[下载地址](http://www.lfd.uci.edu/~gohlke/pythonlibs/),，在网页中搜索twisted找到其对应的whl包Twisted‑18.4.0‑cp36‑cp36m‑win_amd64.whl并下载,根据你的Python的版本选择合适的包，名称中间的cp36是python3.6的意思，amd64是python的位数。  

4. 下载完成后使用cmd打开windows的命令行窗口，进入whl包所在的文件夹执行如下命令：pip install [whl]，[whl]是whl包的名字，即：
  ```
  pip install Twisted-17.1.0-cp36-cp36m-win_amd64.whl  
  ```  
  Scrapy包需要其所有依赖的包安装完成后才能进行安装，现在还不能安装  
  
  5. scrapy依赖lxml包，需要先安装lxml包，lxml包依赖libxml2，libxml2-devel，所以安装lxmllibxml2， libxml2-devel。幸运的是之前我之前已经安装过lxml   
  
  6. 所有准备工作做完，中医可以安装scrapy包了，进入Scrapy-1.3.3-py2.py3-none-any.whl所在的目录  
  ```
  pip install Scrapy-1.3.3-py2.py3-none-any.whl  
  ```
  
  7. Successfully ! 先别急着撒花，是否真的安装成功了，还需要验证，输入scrapy -h，出现以下显示，恭喜你安装成功了：
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
  
  5. 爬虫文件生成后，需要在items.py中编写属性字段，打开瞧瞧吧：
  ```
  class YugaopianItem(scrapy.Item):
    name = scrapy.Field()
    pub_date = scrapy.Field()
    movie_cover = scrapy.Field()
    url = scrapy.Field()
    img_urls = scrapy.Field()
    image_paths = scrapy.Field()
    actor = scrapy.Field()
    director = scrapy.Field()
    desc = scrapy.Field()
   ```
   字段类型类似于字典，可以直接使用key-value的方式设值和获取   
   
  6. 打开aiqiyispider.py文件，要注意几个重要的属性：
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
   
   7. 到这里爬虫文件就编写完成了，如果急于看结果的话，通过运行如下命令：
   ```
   scrapy crawl aiqiyispider -o  aiqiyi.json
   ```
   过一会就可以看到在项目下生成了aiqiyi.json文件，但一般不这么做，通常的做法是在管道文件中处理爬取的结果。  
   
   8. 这个项目中可以看到有两个管道文件，一个用来处理爬取的文字信息（pipelines.py），一个用于下载图片（MyImagePipelines.py）。先看看pipelines.py，如下：
   ```
   class YugaopianPipeline(object):              # 继承object
    def __init__(self):
        self.file = open("yugaopian.json", mode="w", encoding="utf-8")  # 在初始化方法中以写的方式打开json文件，注意编码使用utf-8

    def process_item(self, item, spider):               # 所有爬取的结果都会进入这个方法中，所以方法名不能变
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"  # 将爬取的item转换成json格式，dict方法将item转换成字典
        self.file.write(content)                                      # 将转换后的结果写入文件中
        return item                                                   # 特别注意，一定不能少了return，否则爬虫调度器不知道将如何处理

    def close_spider(self, spider):                                   # 关闭文件
        self.file.close()
   ```
    
 接下来在看看MyImagePipelines.py文件。
   
   ```
    class MyImagePipeline(ImagesPipeline):                   # 继承ImagesPipeline，要处理图片下载，必须继承这个类
    def get_media_requests(self, item, info):                # 爬虫获取图片链接后，会第一时间回调到这个方法，这个方法也是名字不能变
        for url in item['img_urls']:                         
            yield scrapy.Request(url)                        # 将每一个图片请求在发出去    

    def item_completed(self, results, item, info):           # 下载完成后回调到这个方法，可以在这里对item进行处理，修改名字、丢弃等操作 
        image_paths = [x['path'] for ok, x in results if ok] # 这个表达式值得好好推导
        if not image_paths:
            raise DropItem("Item contains no images")        # 丢弃
        item['image_paths'] = image_paths
        return item                                          # 同样需要return    
   ```
  
 9. 管道文件完成后，不要急于运行命令，还有一个重要的文件需要设置，否则将不会有任何结果。想必你已经猜到了，这个文件就是settings.py,打开文件看看哪些地方要注意：
 ```
 USER_AGENT = 'yugaopian (+http://www.yourdomain.com)'  # 设值user_agent请求头，模仿浏览器行为
 ROBOTSTXT_OBEY = True                                  # 设值ROBOTSTXT_OBEY是否开启，一般设置为False
 IMAGES_STORE = "F:\\python\\download\\yugaopian"       # 下载图片存储地址，如果项目中不需要下载图片，可以不设置
 ITEM_PIPELINES = {
      'yugaopian.MyImagePipelines.MyImagePipeline': 1,  # 开启管道文件，后面的值越小，代表优先级越高，可以设置多个管道文件，默认被注释掉，一定要
      'yugaopian.pipelines.YugaopianPipeline': 300,     # 记得打开
 }  
```

10. 到这里就可以愉快的运行启动爬虫命令，见证奇迹的时刻到了，铛铛铛:smirk::smirk::smirk:
```
scrapy crawl aiqiyispider
```
11.最后再说一点，如果需要在程序运行的时候加参数，可以这样做： 
```
class aiqiyispiderSpider(scrapy.Spider):
    name = 'aiqiyispider'                                   # name是爬虫项目唯一的标识，同一个项目中一定不要使用同一个name
    allowed_domains = ['www.yugaopian.cn']                  # 这个可选      
    def __init__(self, text=None, *args, **kwargs):
        super(LovespiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.yugaopian.cn/allmovies?text=%s' % text] # 爬虫启动时第一个爬取的网址，这里可以用列表，也可以用元组，元组注意加逗号
```
然后运行命令的时候加入-a text=动作,类似这样：  
```
scrapy crawl aiqiyispider -a text=动作
```

###### 说明：到这里整个爬虫就算完成了，当然scrapy功能远不止这些，可以通过[scrapy中文网](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)学习。

注意事项
---
1. scrapy的安装比较麻烦，不能直接通过命令来安装，需要先下载whl文件。  
2. scrapy作为爬虫项目比较简单，只需要编写爬虫文件，进行简单的配置就可以了。但我们不能认为scrapy的功能就仅仅于此，它的功能远比我们想象的强大。  
3. 爬虫中提取规则用到xpath语法，因此需要了解xpath的用法，推荐网站[菜鸟教程](http://www.runoob.com/xpath/xpath-syntax.html)。有两个语法注意下：
* /a/following-sibling::a  # 获取a节点后所有兄弟节点（包含a标签）
* /a/following-sibling::a[1] # 获取a节点后包含a标签的第一个兄弟节点
4. xpath中所有元素角标都是从1开始，区别于Python从0开始
5. scrapy可以保存的文件格式有四种，json/csv/xml/JSON lines  
6. scrapy的其他功能，如[暂停/恢复 爬虫](http://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/jobs.html)都是很有用的功能。

写在最后
---
scrapy爬虫项目写完了，但我却越发觉得scrapy的强大，正所谓："越是对知识的渴望，越会体会到知识的无穷尽"。要想彻底的掌握这个框架，必须多练，多看文档，踩的坑越多，掌握的就越熟练。最后一句话送给和我一样的人"人丑就要多看书！":yum::yum::yum::yum:
 

 
 





