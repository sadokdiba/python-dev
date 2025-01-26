import pandas as pd

df = pd.read_csv("./user-details.csv")
# user_list_dict = {row["First Name"]:row["Email"] for (index, row) in df.iterrows() if row.Timezone == 'America/Los_Angeles'}
# print(user_list_dict)
# new_data = pd.DataFrame(list(user_list_dict.items()), columns=["First Name", "Email"])

filtered_df = df[df["Timezone"] == "America/Los_Angeles"]

filtered_df.to_csv("./LA_users.csv")