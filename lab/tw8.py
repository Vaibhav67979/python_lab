import pandas as pd

if __name__ == '__main__':
    myData = pd.read_csv("studentData.csv")
    print(myData.to_string())
    print("   ............Table Columns...........   ")
    print("===============================================")
    for col in myData.columns:
        print(col + "\t\t", end='')
    colName = input("\nEnter column name : ")
    print(myData.loc[:, colName].unique())
    print(myData.groupby(colName)[colName].count())
    print("Total rows in DFrame : " + str(myData.shape[0]))
