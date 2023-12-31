import os
def create_categories_dict(df):
    # Create a DataFrame with supplier and main_category
    df_supplier_main_category = df[['supplier', 'main_category']]

    # Convert the DataFrame to a JSON string
    json_str = df_supplier_main_category.to_json(orient='records')

    # Write the JSON string to a file
    with open('supplier_main_category.json', 'w') as f:
        f.write(json_str)
    # return json file absulote path
    return os.path.abspath('supplier_main_category.json')