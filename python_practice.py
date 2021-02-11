#print ("Hello world")
#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
 #   print(counties[1])
#if counties[3] != 'Jefferson':
#    print(counties[2])
counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not in the list of counties.")
#if "Arapahoe" in counties and "El Paso" in counties:
    #print("Arapahoe and El Paso are in the list of counties.")
#else:
    #print("Arapahoe or El Paso is not in the list of counties.")
#for county in counties:
    #print(county)
voting_data = []
voting_data.append({"county":"Arapahoe","voters":422829})
voting_data.append({"county":"Denver","voters":463353})
voting_data.append({"county":"Jefferson","voters":432438})

for county_votes in voting_data:
    print(f"{county_votes['county']} has")
    print(f"{county_votes['voters']} registered voters.")
   

counties_dict = {"Arapahoe": '422829', "Denver": '463353', "Jefferson": '432438'}

#for county, voters in counties_dict.items():
    #print(county + " county has", voters + " voters")
#for county, voters in counties_dict.items():
   # print(f"{county} county has {voters} registered voters.")
#for county_votes in voting_data: 
   # print(county_votes)
#for county_votes in voting_data: 
   # print(county_votes['voters'])
