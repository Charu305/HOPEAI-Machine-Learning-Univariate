class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual

    def freqTable(colunName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","Cusum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cusum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable

    def Univariate(dataset,qual):
    Descriptive = pd.DataFrame(index=['Mean','Median','Mode','Q1:25th','Q2:50th','Q3:75th'
                                      ,'99%','Q4:100th','IQR','1.5rule','Lesser','Greater',
                                      'Min','Max','kurtosis','skew','Var','Std'],columns=qual)
    for columnName in qual:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            Descriptive[columnName]["Mean"]=dataset[columnName].mean()
            Descriptive[columnName]["Median"]=dataset[columnName].median()
            Descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            Descriptive[columnName]["Q1:25th"]=dataset.describe()[columnName]["25%"]
            Descriptive[columnName]["Q2:50th"]=dataset.describe()[columnName]["50%"]
            Descriptive[columnName]["Q3:75th"]=dataset.describe()[columnName]["75%"]
            Descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            Descriptive[columnName]["Q4:100th"]=dataset.describe()[columnName]["max"]
            Descriptive[columnName]["IQR"]=Descriptive[columnName]["Q3:75th"]-Descriptive[columnName]["Q1:25th"]
            Descriptive[columnName]["1.5rule"]=1.5*Descriptive[columnName]["IQR"]
            Descriptive[columnName]["Lesser"]=Descriptive[columnName]["Q1:25th"]-Descriptive[columnName]["1.5rule"]
            Descriptive[columnName]["Greater"]=Descriptive[columnName]["Q3:75th"]+Descriptive[columnName]["1.5rule"]
            Descriptive[columnName]["Min"]=dataset.describe()[columnName]["min"]
            Descriptive[columnName]["Max"]=dataset.describe()[columnName]["max"]
            Descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            Descriptive[columnName]["skew"]= dataset[columnName].skew()
            Descriptive[columnName]["Var"] = dataset[columnName].var()
            Descriptive[columnName]["Std"] = dataset[columnName].std()
    return Descriptive
    
    def FindOutlier(dataset,qual,Descriptive):
        lesser=[]
        greater=[]
        
        for columnName in qual:
            if Descriptive[columnName]['Min']<Descriptive[columnName]['Lesser']:
                lesser.append(columnName)
            if Descriptive[columnName]['Max']>Descriptive[columnName]['Greater']:
                greater.append(columnName)
        return lesser,greater
    def ReplaceOutliers(dataset,lesser,greater,Descriptive):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<Descriptive[columnName]['Lesser']]=Descriptive[columnName]['Lesser']
        for columnName in greater:
            dataset[columnName][dataset[columnName]>Descriptive[columnName]['Greater']]=Descriptive[columnName]['Greater']
        return dataset
    