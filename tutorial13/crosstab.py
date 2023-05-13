import pandas as pd
df = pd.read_excel("resources/survey_tut13.xls")
print(df)
print("========================================")

# Using crosstable
new_df = pd.crosstab(df.Nationality, df.Handedness)
print(new_df)

print("========================================")
# The margin argument

new_df = pd.crosstab(df.Sex, df.Handedness, margins = True)
print(new_df)
print("========================================")

# Using more than two variable
new_df = pd.crosstab(df.Sex, [df.Handedness, df.Nationality], margins = True)
print(new_df)

