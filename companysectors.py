import matplotlib.pyplot as plt
#from pymongo import MongoClient
import pymongo

import pandas
import collections

def get_companies():
	# Connect to the database
	client = pymongo.MongoClient('ds159125-a0.mlab.com:59125', username='dave_GFG', password='Yjhh639Da8ne',authSource='greenfinancialguide_db',authMechanism='SCRAM-SHA-1')
	db = client.greenfinancialguide_db
		
	# Retrieve all companies from the 'companies' collection in the database
	companies = db.companies.find({})
		
	return companies

if __name__ == '__main__':
	companies=get_companies()

	sector_count_list=[]
	sector_name_list=[]
	
	for company in companies:
		# From a python perspective a company looks like a dictionary, and we need key 'sector_analysis'
		# The value of company['sector_analysis'] is a value (primary_sector) and a list (industry_sectors)

		company_name=company['name']
		primary_sector=company['sector_analysis']['primary_sector']
		industry_sectors=company['sector_analysis']['industry_sectors']
		
		#print(company_name, ' : ',primary_sector, ' : ', industry_sectors, '!', len(industry_sectors) )

		if primary_sector is '':
			print('Company: ', company_name,' has NO PRIMARY SECTOR')

		# Add the number of industry_sectors to our frequency list
		sector_count_list.append(len(industry_sectors))
		sector_name_list.append(primary_sector)

primary_counts = collections.Counter(sector_name_list)

print(primary_counts)

df = pandas.DataFrame.from_dict(primary_counts, orient='index')

axes=df.plot(kind='bar',title='Frequency of primary sectors',legend=False)
axes.set_xlabel("Primary sector")
axes.set_ylabel("Number of Instances in Companies")

list_of_bins=list(range(0,31))
plt.style.use('ggplot')
plt.hist(sector_count_list, bins=list_of_bins)
plt.show()
