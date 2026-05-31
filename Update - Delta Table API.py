# Databricks notebook source
# MAGIC %md
# MAGIC ![image_1780239358709.png](./image_1780239358709.png "image_1780239358709.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1780239433693.png](./image_1780239433693.png "image_1780239433693.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ![image_1780239541655.png](./image_1780239541655.png "image_1780239541655.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step by Step Demo

# COMMAND ----------

from delta.tables import DeltaTable

# COMMAND ----------

data = [
    (101, "John", 5000),
    (102, "David", 6000),
    (103, "Smith", 7000)
]

df = spark.createDataFrame(data, ["employee_id", "employee_name", "salary"])
df.show()

# COMMAND ----------

df.write.format("delta").save("/Volumes/demoyt/default/volume_demo/employee_delta")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Load Delta Table Using Delta Table API

# COMMAND ----------

dt = DeltaTable.forPath(spark, "/Volumes/demoyt/default/volume_demo/employee_delta")

# COMMAND ----------

# MAGIC %md
# MAGIC ### - Update Single Records Example

# COMMAND ----------

dt.update(
    condition= "employee_id = 102",
    set = {"salary":"8000"}
)

# COMMAND ----------

spark.read.format("delta").load("/Volumes/demoyt/default/volume_demo/employee_delta").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Update MUltiple Records (NO Condition)

# COMMAND ----------

dt.update(
    set ={"salary":"salary*1.10"}

)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Update Multiple Columns

# COMMAND ----------

dt.update(
    condition = "employee_id = 101",
    set = {
        "salary":"6500",
        "employee_name":"'John Miller'"
    }
)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

