import json
import pandas as pd

df = pd.read_excel('קטלוג.xlsx')
item_name = df.columns[2]
supplier = df.columns[-1]
main_category = df.columns[-3]
df = df.dropna(axis=0, subset=main_category)

# Step 1: Create dictionaries
supplier_dict = {v: f"{i:03}" for i, v in enumerate(df[supplier].unique())}
main_category_dict = {v: f"{i:03}" for i, v in enumerate(df[main_category].unique())}

# Create a dictionary for each combination of supplier, main_category, and sub_category
item_name_dict = {}
for supplier_val in df[supplier].unique():
    for main_category_val in df[df[supplier] == supplier_val][main_category].unique():
        combination_df = df[(df[supplier] == supplier_val) & (df[main_category] == main_category_val)]
        item_name_dict[(supplier_val, main_category_val)] = {v: f"{i:03}" for i, v in
                                                             enumerate(combination_df[item_name].unique())}

# save dictionaries to json files for later use names in utf-8 format
with open('supplier_dict.json', 'w', encoding='utf-8') as f:
    json.dump(supplier_dict, f, ensure_ascii=False)
with open('main_category_dict.json', 'w', encoding='utf-8') as f:
    json.dump(main_category_dict, f, ensure_ascii=False)


# Modify the create_id function
def create_id(row):
    supplier_code = supplier_dict[row[supplier]]
    main_category_code = main_category_dict[row[main_category]]
    item_name_code = item_name_dict[(row[supplier], row[main_category])][row[item_name]]
    return supplier_code + main_category_code + item_name_code


# Apply function
for i, row in df.iterrows():
    df.loc[i, 'id'] = create_id(row)

print(df)
