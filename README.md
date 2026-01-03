import requests
import json
import pandas as pd

def estrai_dati(numero_pagine, init_page=480): #data extraction 
    
    def altridic(dataframe):
        m=[]
        for x in dataframe:
            f=[]
            listanomi=[]
            for a in x:
                if type(x[a]) is dict:
                    for k,v in x[a].items():
                        f.append(v)
                        listanomi.append(k)
            m.append(f)
        df2=pd.DataFrame(m)
        df2=df2.iloc[:,:len(listanomi)]
        df2.columns=listanomi
        return df2
    
    def leggi_df(dataframe):
        a=altridict(dataframe)
        s=pd.DataFrame(dataframe)
        result=pd.concat([a,s], axis=1)
        display(results)
        return results
    
    listadef=[]
    for i in range(numero_pagine):
        listafatture=[]
        dinamic="enter_your_url"+str(init_page)
        init_page+=1
        url=dinamic
        
        headers = {
            "Accept":"application/json",
            "Authorization": "Bearer enter_your_API_credentials"
        }
        
        response=requests.get(url, headers=headers)
        
        if response.json()["data"]==[]:
            break
        else:
            listafatture.append(response.json()["data"])
            
        for xs in listafatture:
            for x in xs:
                listadef.append(x)
                
        for x in listadef:
            for a in x["payment_list"]:
                for k,v in a.items():
                    x.update({k:v})
                    
        for x in listadef:
            for pa in x["payment_account"]:
                for k,v in pa.items():
                    x.update({str(k):str(v)})
                    
    return leggi_df(listadef)
