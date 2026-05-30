# Databricks notebook source
# MAGIC %md
# MAGIC ![image_1780149137100.png](./image_1780149137100.png "image_1780149137100.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1780150347808.png](./image_1780150347808.png "image_1780150347808.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1780151442076.png](./image_1780151442076.png "image_1780151442076.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ### The 4-Step Execution Pipeline
# MAGIC - 1.Explore
# MAGIC - 2.Import
# MAGIC - 3.Create instance
# MAGIC - 4.Execute

# COMMAND ----------

data = [
    (1, "C101", "Laptop", 50000, "2024-01-01", None),
    (2, "C102", "Mobile", 20000, "2024-01-02", "NEWYEAR"),
    (3, "C103", "Tablet", None, "2024-01-03", None),  # missing price
    (4, "C101", "Laptop", 50000, "2024-01-01", None), # duplicate
    (5, "C104", "Headphones", 2000, "2024-01-04", None),
    (6, "C105", "Camera", 30000, "2024-01-05", "SALE10")
]

columns = ["order_id", "customer_id", "product", "amount", "order_date", "coupon"]

df= spark.createDataFrame(data, columns)
df.write.format("delta").mode("overwrite").saveAsTable("DemoYT.default.demo_order")
df.display()

# COMMAND ----------

spark.read.table("DemoYT.default.demo_order").display()


# COMMAND ----------

from delta.tables import DeltaTable

# COMMAND ----------

dt = DeltaTable.forName(spark,"DemoYT.default.demo_order")

# COMMAND ----------

dt.delete('order_id = 1')

# COMMAND ----------

# MAGIC %md
# MAGIC **Spark column expression **method****

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

dt.delete(col("customer_id")=="C102")

# COMMAND ----------

# MAGIC %md
# MAGIC ## DataFrame Approach

# COMMAND ----------

df = spark.read.table("DemoYT.default.demo_order")

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.filter("product != 'Tablet'")

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("DemoYT.default.demo_order")

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1780151564851.png](./image_1780151564851.png "image_1780151564851.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1780153782815.png](./image_1780153782815.png "image_1780153782815.png")

# COMMAND ----------



# COMMAND ----------

