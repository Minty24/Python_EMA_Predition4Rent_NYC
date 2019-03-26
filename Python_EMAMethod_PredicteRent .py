
# coding: utf-8

# #Tackle each unique SpaceID and predict for Q1 2019’s rent value 
# #given a time series, parameters alpha (smoothing component) and beta (trend component), 
# #program return series of smoothed observations plus next forecasted value
# 

# In[ ]:

def double_exponential_smoothing(rents, alpha, beta):#alpha=level, beta= trend
    result = [rents[0]]
    if len(rents) <= 5:
        return rents[len(rents)-1]
    
    result= [rents[0]]
    for n in range(1, len(rents)+1):
        if n == 1:
            level, trend = rents[0], rents[1] - rents[0]
        if n >= len(rents):
          value = result[-1]
        else:
          value = rents[n]
        last_level, level = level, alpha*value + (1-alpha)*(level+trend)
        trend = beta*(level-last_level) + (1-beta)*trend
        result.append(level+trend)
    return result[len(result)-1]


# In[ ]:

import pandas as pd
reading file, created empty list for holding result 
data_from_file = pd.read_csv("Rent.csv", low_memory=False)
listofSpaceIDS = data_from_file.SpaceID.unique().tolist()
SId = []
ObservedRents= []
Output = []


# In[ ]:

#Define the datas from prediction, alpha, beta

alpha= 0.9
beta= 0.9
for spaceID in listofSpaceIDS:
    print (spaceID)
    SId.append(spaceID)
    
    space_row = data_from_file[data_from_file.SpaceID == spaceID]
    list_rent = space_row['GrossRent'].tolist()
    print (list_rent)
    ObservedRents.append(list_rent)


# In[ ]:

#call for result (predicted rent for next quarter) with this list as parameter.... 
final= double_exponential_smoothing(list_rent, alpha, beta)

print(final)

Output.append(final)
    


# In[ ]:

#Output the result containing only variables of SpaceID, Year&QuarterReference, GrossRent 

df = pd.DataFrame({'spaceid': SId, 'Observed Rents': ObservedRents, 'Fittedand Estimation Rents': Output})

