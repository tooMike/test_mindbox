from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, lit

# Создание SparkSession
spark = SparkSession.builder \
    .appName("ProductCategoryPairs") \
    .getOrCreate()


# Создание DataFrames
products_df = spark.createDataFrame(
    products_data,
    ["product_id", "product_name"]
)
categories_df = spark.createDataFrame(
    categories_data,
    ["category_id", "category_name"]
)
product_categories_df = spark.createDataFrame(
    product_categories_data,
    ["product_id", "category_id"]
)


# Метод для получения всех пар «Имя продукта – Имя категории» и продуктов
# без категорий
def get_product_category_pairs_and_unpaired_products(
        products_df,
        categories_df,
        product_categories_df
):
    # Найти все пары «Имя продукта – Имя категории»
    product_category_pairs_df = product_categories_df \
        .join(broadcast(products_df), "product_id") \
        .join(broadcast(categories_df), "category_id") \
        .select("product_name", "category_name")

    # Найти все продукты, у которых нет категорий и добавить столбец с None
    # для категории
    products_without_categories_df = products_df \
        .join(product_categories_df, "product_id", "left_anti") \
        .select("product_name", lit(None).alias("category_name"))

    # Объединить оба DataFrame
    result_df = product_category_pairs_df.union(products_without_categories_df)

    return result_df


# Вызов метода и показ результата
result_df = get_product_category_pairs_and_unpaired_products(
    products_df,
    categories_df,
    product_categories_df
)
result_df.show()

# Остановить SparkSession
spark.stop()
