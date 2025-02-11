from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SocialMediaAnalysis").getOrCreate()
data = spark.read.json("data/social_media_data.json")
data_filtered = data.select("user", "text", "timestamp").filter(col("lang") == "en")
data_filtered.show()
