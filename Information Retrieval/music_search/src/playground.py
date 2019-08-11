from elasticsearch import Elasticsearch

es = Elasticsearch()

print(es.indices.get_alias("*"))
