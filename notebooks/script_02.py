# Databricks notebook source
# DBTITLE 1,Testing Connection
dbutils.fs.ls("/mnt/data/inbound")

# COMMAND ----------

# DBTITLE 1,Reading RAW Data
# MAGIC %scala
# MAGIC val path = "dbfs:/mnt/data/inbound/dados_brutos_imoveis.json"
# MAGIC val data = spark.read.json(path)
# MAGIC display(data)

# COMMAND ----------

# DBTITLE 1,Removing Images and User Data for ADs
# MAGIC %scala
# MAGIC val ad_data = data.drop("imagens", "usuario")
# MAGIC display(ad_data)

# COMMAND ----------

# DBTITLE 1,Creating ID Column
# MAGIC %scala
# MAGIC import org.apache.spark.sql.functions.col
# MAGIC
# MAGIC val df_bronze = ad_data.withColumn("id", col("anuncio.id"))
# MAGIC display(df_bronze)

# COMMAND ----------

# DBTITLE 1,Saving File in Azure Deltalake
# MAGIC %scala
# MAGIC val path = "dbfs:/mnt/data/bronze/imoveis"
# MAGIC df_bronze.write.format("delta").mode(SaveMode.Overwrite).save(path)
