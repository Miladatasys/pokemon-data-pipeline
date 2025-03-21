import great_expectations as ge

# Load data
df = ge.read_csv("./data/ditto_data.csv")

# Define expectations
df.expect_column_values_to_not_be_null("name")
df.expect_column_values_to_be_unique("name")
df.expect_column_values_to_be_between("height", min_value=0)
df.expect_column_values_to_be_between("weight", min_value=0)

# Validate
validation_result = df.validate()
print(validation_result)