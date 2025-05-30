from elasticsearch import Elasticsearch
from extract_sql import extract_sql
from score_sql import score_sql

# Elasticsearch connection
client = Elasticsearch(
    "https://my-elasticsearch-project-cfe5ad.es.us-east-1.aws.elastic.cloud:443",
    api_key="Zl9pZklwY0Iwa19MS0lfYVVKN0U6RVNIZGVWeHVndVZCcnc3MkhQUy1Odw=="
)

index_name = "sql-vuln"

# Extract SQL lines
snippets = extract_sql("data/sample_queries.sql")

# Add scores and index
for snippet in snippets:
    snippet["score"] = score_sql(snippet["code"])
    client.index(index=index_name, document=snippet)

print("✅ SQL vulnerabilities indexed to Elasticsearch.")
