def read_data(path,data):
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    import pandas as pd
    import os
    os.chdir(path)
    data= pd.read_csv(data,na_values=['-','?','!','#','$','%','&','/','|','(',')','()','*',',','.',':',';','<','=','>','?','@','{}','{','}','`','~','^'])
    return data


def view_data(dataset):
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    print('\n\n')
    no_of_rows= int(input('please mention the no. of rows u want to view: '))
    if no_of_rows > len(dataset):
        print('\n\n')
        no_of_rows=input('the no. entered is greater than the no. of rows in the dataset: ')
    elif no_of_rows<= len(dataset):
        print(dataset.head(no_of_rows))
    elif no_of_rows==0:pass





def null_check(dataset):
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    print('\n\n\n')
    print('Here is the list of null values found:')
    print(dataset.isnull().sum())
    
    if dec=='y':
        data=dataset.dropna()
        print('\n\n\n')
        view=input("do you want to review the data? ansewr in"+"("+GREEN+BOLD+"y"+"/"+RED+BOLD+"n"+")"+" :  "+END)
        if view=='y':
            view_data(dataset)
        else:
            pass
    elif dec=='n':
        data=dataset
    return data
    
            
            
        
        
    





def binning(data):
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    import pandas as pd
    print('Below Given are The List of'+GREEN+BOLD+' COLUMNS/Feature names: \n'+END)
    print(data.columns)
    print("Please provied the list of index no.s of the perticular columns that"+GREEN+BOLD+" you want to do binning:\n"+END)
    print(RED+BOLD+"Maximum NO. OF COLUMNS TO BE SELECTED AT A TIME:: "+GREEN+BOLD+"3"+END)
    c=list(map(int, input("index no.s of the columns that YOU  WANT BINS FOR : ").split()))
    if len(c)!=0:
        while True:
            try:
                if len(c)==1:
                    h=int(input("Enter the no. bins u want: "))
                    j=c[0]
                    x=pd.qcut(data.iloc[:,j],h)
                    binned=data.drop(data.columns[c],axis=1)
                    binned1=pd.concat([binned,x],axis=1)
                    return binned1
                    break
                if len(c)==2:
                    h=int(input("Enter the no. bins u want for"+RED+" 1st"+" slected column: "+END))
                    h1=int(input("Enter the no. bins u want for"+GREEN+" 2nd"+" slected column: "+END))
                    j=c[0]
                    x=pd.qcut(data.iloc[:,j],h)
                    j=c[1]
                    y=pd.qcut(data.iloc[:,j],h1)
                    binned=data.drop(data.columns[c],axis=1)
                    binned1=pd.concat([binned,x],axis=1)
                    binned2=pd.concat([binned1,y],axis=1)
                    return binned2
                    break
                if len(c)==3:
                    h=int(input("Enter the no. bins u want for"+RED+" 1st"+" slected column: "+END))
                    h1=int(input("Enter the no. bins u want for"+GREEN+" 2nd"+" slected column: "+END))
                    h2=int(input("Enter the no. bins u want for"+BLUE+" 3RD"+" slected column: "+END))
                    j=c[0]
                    z=pd.qcut(data.iloc[:,j],h)
                    j=c[1]
                    y=pd.qcut(data.iloc[:,j],h1)
                    j=c[2]
                    x=pd.qcut(data.iloc[:,j],h2)
                    binned=data.drop(data.columns[c],axis=1)
                    binned1=pd.concat([binned,z],axis=1)
                    binned2=pd.concat([binned1,y],axis=1)
                    binned3=pd.concat([binned2,x],axis=1)
                    return binned3
                    break
            except ValueError:
                print("The no. of bins selected is not exicutable so please select again: ")
                
                
            
def dummy(data):
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    import pandas as pd
    print('\n\n')
    print('Below Given are The List of'+GREEN+BOLD+' COLUMNS/Feature names: \n\n'+END)
    print(data.columns)
    print("Please provied the list of index no.s of the perticular columns that"+RED+BOLD+" YOU DON'T WANT to make dummies:"+END)
    print(RED+BOLD+"Maximum NO. OF COLUMNS TO BE SELECTED AT A TIME:: "+GREEN+BOLD+"3"+END)
    c=list(map(int, input("index no.s of the columns that YOU DON'T WANT DUMMIES: ").split()))
    data_getting_dummies= data.drop(data.columns[c],axis=1)
    dummied=pd.get_dummies(data_getting_dummies)
    if len(c) != 0:
        for j in c:
            if len(c)==1:
                x=data.iloc[:,j]
                dummied=pd.concat([dummied,x],axis=1)
            if len(c)==2:
                    y=data.iloc[:,j]
                    dummied=pd.concat([dummied,y],axis=1)
            if len(c)==3:
                    z=data.iloc[:,j]
                    dummied=pd.concat([dummied,z],axis=1)
    print(GREEN+"PRE PROCESSING IS DONE!!!"+END)                
    return dummied


def auto_process():
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    path=input("Please enter the location path of the dataset u want to pre-process: ")
    dataset=input("please enter the name of the dataset: ")
    data=read_data(path,dataset)
    q=input("Do you want to view the data?ansewr in"+"("+GREEN+BOLD+"y"+"/"+RED+BOLD+"n"+")"+" :  "+END)
    if q == 'y': view_data(data)
    elif q== 'n':pass
    df=null_check(data)
    r=input("Do you want to perform binning on the data ? ansewr in"+"("+GREEN+BOLD+"y"+"/"+RED+BOLD+"n"+")"+" :  "+END)
    if r=='y': 
        df1=binning(df)
        t=input("Do you want to make dummies for any for any colunms in the data ? ansewr in"+"("+GREEN+BOLD+"y"+"/"+RED+BOLD+"n"+")"+" :  "+END)
        if t=='y':
            df2=dummy(df1)
            return df2
    elif r=='n':
        t=input("Do you want to make dummies for any colunms in the data ? ansewr in"+"("+GREEN+BOLD+"y"+"/"+RED+BOLD+"n"+")"+" :  "+END)
        if t=='y':
            df2=dummy(df)
            return df2
        elif t=='n':return df
        
