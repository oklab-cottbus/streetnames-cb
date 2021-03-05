import get_gender as gg
import pandas as pd

magdeburg_names = pd.read_csv("names-magdeburg.csv")
for name in magdeburg_names["Name"]:
  data = gg.get_gender(name)
  try:
    df_magdeburg_test_names = df_magdeburg_test_names.append(pd.DataFrame.from_dict(data))
  except Exception:
    df_magdeburg_test_names = pd.DataFrame.from_dict(data)
  df_magdeburg_test_names.to_csv("names-magdeburg_test.csv",index=False)
  print(data["Name"]+data["Gender"]+data["Information"])
 
 
