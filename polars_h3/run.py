import polars as pl
from polars_h3 import H3


data = {"lat": [34.6432], "lag": [134.9976]}
df = pl.DataFrame(data, schema=[("lat", pl.Float64), ("lag", pl.Float64)])

print(
    df.with_columns(
        h3=pl.col("lat").h3.geo_to_h3("lag"),
    )
)
