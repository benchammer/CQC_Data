# CQCRatings.py uses the CQC API to access the CQC overall and key question ratings for providers
# specified in CQCproviders.csv. The data is written to CQCdataOutput.csv

# Example URL: https://api.cqc.org.uk/public/v1/providers/RL4?partnerCode=ADVISORYBOARD

import csv, requests, json

# Variables
url='https://api.cqc.org.uk/public/v1/providers/'
providerFile = 'CQCproviders.csv'
resultFile = 'CQCdataOutput.csv'
delim = '; '
partnerCode = '?partnerCode=ADVISORYBOARD' # Requested by OGL 

print('Running...')

# Open the output file the data will be written to
outfile = open(resultFile, 'w', newline='')
writer = csv.writer(outfile, delimiter=';')

# Write headers to the file
writer.writerow(['CQC ID' + delim + 'Provider' + delim + 'Website' + delim + 'Rating Date' + delim + 'Overall Rating' 
+ delim + 'Safe' + delim + 'Well-Led' + delim + 'Caring' + delim + 'Responsive' + delim + 'Effective' + delim + 'JSON'])

# Loop through each CQC provider and read in the JSON data from CQC. Then write to the output file
for row in csv.reader(open(providerFile), delimiter=','):
    url2 = url + row[0] + partnerCode
    r = requests.get(url2) # Get the JSON data from the URL
    jdata = json.loads(r.text)
    writer.writerow([jdata['providerId'] + delim + jdata['name'] + delim + jdata['website'] + delim
+ jdata['currentRatings']['reportDate'] + delim + jdata['currentRatings']
['overall']['rating'] + delim + jdata['currentRatings']['overall']['keyQuestionRatings'][0]['rating']
+ delim + jdata['currentRatings']['overall']['keyQuestionRatings'][1]['rating'] + delim + 
jdata['currentRatings']['overall']['keyQuestionRatings'][2]['rating'] + delim + 
jdata['currentRatings']['overall']['keyQuestionRatings'][3]['rating'] + delim + 
jdata['currentRatings']['overall']['keyQuestionRatings'][4]['rating'] + delim + url2
])
outfile.close()

# Print a message to say when the task has completed. Takes up to a minute.
print('Complete')
