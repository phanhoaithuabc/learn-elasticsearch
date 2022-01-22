from elasticsearch import Elasticsearch
from datetime import datetime

es_uri = f"http://localhost:9200/"
elastic_search = Elasticsearch([es_uri])


# es_uri = f"http://vpc-els-rent-semanticsearch-dev-amdkx3baodpgkejgqeze5xomve.us-east-1.es.amazonaws.com:443"
# elastic_search = Elasticsearch([es_uri],
#                         http_auth=("rent-dev", "Rent@12345"),
#                         use_ssl=True,
#                         ca_certs="./AmazonRootCA1.pem")


# elastic_search.indices.create(index = 'search-history-2022-01-17')
# elastic_search.indices.create(index = 'search-history-2022-01-18')
# elastic_search.indices.create(index = 'search-history-2022-01-19')
# elastic_search.indices.create(index = 'rent-sentences-64-2021-11')
# elastic_search.indices.create(index = 'rent-sentences-64-2021-12')
# elastic_search.indices.create(index = 'rent-sentences-64-2022-01')

now = datetime.now()
print(now.year, now.month, now.day)
indices_dict = elastic_search.indices.get_alias("*")
for name, value in indices_dict.items():
    try:
        if ('search-history' in name and \
            (int(name.split('-')[-1]) != now.day or int(name.split('-')[-2]) != now.month)) \
            or (int(name.split('-')[-2]) != now.year and int(name.split('-')[-1]) <= now.month):
            elastic_search.indices.delete(index=name)
    except Exception:
        print(Exception)
