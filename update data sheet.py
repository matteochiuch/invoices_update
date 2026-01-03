def porta_in_sheet(num_pag,inizio):
    
    import requests
    import json
    import pandas as pd
    
    df=estrai_dati(num_pag, inizio)
    
    df1=df["type"].iloc[:,1:2]
    df2=pd.DataFrame(df["number"])
    df2["Empty_column"]=" "
    df2["Status"]=" "
    df2["Scaduta da più di 60 giorni + Core"]=" "
    df2["Assigned User"]=" "
    df2["Team"]=" "
    df4=df["name"].iloc[:,:1]
    df5=df["id"].iloc[:,1:2]
    df6=df["amount"]
    df7=df["status"].iloc[:,1:2]
    df8=df["date"]
    df9=df["due_date"]
    df10=df["paid_date"]
    df11=df["name"].iloc[:,4:5]
    df12=df2.iloc[:,:2]
    df13=df2.iloc[:,2:]
    df=pd.concat([df13,df1,df12,df4,df5,df6,df7,df8,df9,df10,df11])
    df_def=df.astype(str)
    
    !pip install gspread
    
    from google.colab import auth
    from oauth2client.client import GoogleCredentials
    import gspread
    import pandas as pd
    
    auth.authenticate_user()
    
    from google.auth import default
    creds, _ = default()
    gc=gspread.authorize(creds)
    
    spreadsheet_key= "enter your spreadsheet key"
    workbook=gc.open_by_key(spreadsheet_key)
    worksheet=workbook.get_worksheet(0)
    worksheet.clear()
    
    worksheet.update([df.columns.value.tolist()] + df.values.tolist())
