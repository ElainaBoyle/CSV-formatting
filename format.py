import csv

filename = 'datafile.csv'

with open(filename, 'r', newline='') as csvfileR:
    with open('clean.csv', 'w') as csvfileW:
        reader = csv.reader(csvfileR, quoting=csv.QUOTE_NONE)
        writer = csv.writer(csvfileW)
        fields = ['Start Date', 'End Date', 'Program Title', 'Faculty Director', 'Term', 'Number of Participants', 'Country', 'Countries Visited', 'Photos']
        writer.writerow(fields)
        next(reader)
        for row in reader:
            array = []
            startYear = int(row[0][:4])
            endYear = startYear
            startMonth = "00"
            endMonth = "00"
            if ("spring" in row[3]) or ("Spring" in row[3]):
                startYear += 1
                endYear += 1
                startMonth = "03"
                endMonth = "06"
            elif ("winter" in row[3]) or ("Winter" in row[3]):
                endYear += 1
                startMonth = "12"
                endMonth = "03"
            elif ("fall" in row[3]) or ("Fall" in row[3]):
                startMonth = "08"
                endMonth = "11"
            elif ("summer" in row[3]) or ("Summer" in row[3]):
                startMonth = "06"
                endMonth = "08"
            array.append(str(startYear) + "/" + startMonth) #start date
            array.append(str(endYear) + "/" + endMonth) #end date
            array.append(row[2]) #faculty director
            array.append(row[3]) #term
            array.append(row[4]) #number of participants
            array.append(row[5]) #country
            array.append(row[6]) #countries visited
            writer.writerow(array)

csvfileW.close()
csvfileR.close()


    