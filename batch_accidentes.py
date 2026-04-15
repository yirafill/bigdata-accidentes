from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Accidentes").getOrCreate()

df = spark.read.csv("accidentes.csv", header=True, inferSchema=True)

df.printSchema()
df.show(5)

print("Total de registros:", df.count())

print("=== ACCIDENTES POR DEPARTAMENTO ===")
df.groupBy("DEPARTAMENTO").count().show()

print("=== ACCIDENTES POR MUNICIPIO ===")
df.groupBy("MUNICIPIO").count().show()

spark.stop()
