# Lucene, Solr & ElasticSearch

## Concepts

1. Lucene是一套信息检索工具包，并不包含搜索引擎系统，它包含了索引结构、读写索引工具、相关性工具、排序等功能，因此在使用Lucene时仍需要关注搜索引擎系统，例如数据获取、解析、分词等方面的东西。而solr和elasticsearch都是基于该工具包做的一些封装。

2. Solr是一个有HTTP接口的基于Lucene的查询服务器，封装了很多Lucene细节，自己的应用可以直接利用诸如 .../solr?q=abc 这样的HTTP GET/POST请求去查询，维护修改索引。

3. Elasticsearch也是一个建立在全文搜索引擎 Apache Lucene基础上的搜索引擎。采用的策略是分布式实时文件存储，并将每一个字段都编入索引，使其可以被搜索。

4. Lucene使用上更加灵活，但是你需要自己处理搜素引擎系统架构，以及其他附加附加功能的实现。而Solr帮你做了更多，但是是一个处于高层的框架，Lucene很多新特性不能及时向上透传，所以有时候可能发现需要一个功能，Lucene是支持的，但是Solr上已经看不到相关接口。

## Relation and Differences

### 联系

1. solr和elasticsearch都是基于Lucene实现的！

### 区别

1. solr利用zookpper进行分布式管理，而elasticsearch自身带有分布式协调管理功能；
2. solr比elasticsearch实现更加全面，solr官方提供的工恩能够更多，而elasticsearch本身更注	重于核心功能，高级功能多由第三方插件提供；
3. solr在传统的搜索应用中表现好于elasticsearch，而elasticsearch在实时搜索应用方面比solr表现好！


## Reference

1. [Lucene、solr以及elasticsearch之间的区别和联系](https://blog.csdn.net/weixin_37886463/article/details/79447063)