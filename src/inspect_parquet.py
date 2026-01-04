import pyarrow.parquet as pq

pf = pq.ParquetFile("data/raw/complaint_embeddings.parquet")
print(pf.schema)
