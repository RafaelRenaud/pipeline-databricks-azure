# Databricks notebook source
# DBTITLE 1,Checking Bronze File
dbutils.fs.ls("/mnt/data/bronze")

# COMMAND ----------

# DBTITLE 1,Reading Bronze Dataset
# MAGIC %scala
# MAGIC val path = "dbfs:/mnt/data/bronze/imoveis"
# MAGIC val df_bronze = spark.read.format("delta").load(path)
# MAGIC display(df_bronze)

# COMMAND ----------

# DBTITLE 1,Creating Detailed Data
# MAGIC %scala
# MAGIC val detailed_data = df_bronze.select("anuncio.*", "anuncio.endereco.*")
# MAGIC display(detailed_data)

# COMMAND ----------

# DBTITLE 1,Removing Unnecessary Columns
# MAGIC %scala
# MAGIC val df_silver = detailed_data.drop("caracteristicas","endereco")
# MAGIC display(df_silver)

# COMMAND ----------

# MAGIC %scala
# MAGIC val path = "dbfs:/mnt/data/silver/imoveis"
# MAGIC df_silver.write.format("delta").mode("overwrite").save(path)
