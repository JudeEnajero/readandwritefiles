import csv

id_dict = {"250": 0, "251": 0, "252": 0, "253": 0, "254": 0, "255": 0, "256": 0, "257": 0, "258": 0, "259": 0, "260": 0, "261": 0}

with open('sales.csv', 'r') as file:
    reader = csv.reader(file)
    
    for line in reader:
        for key in id_dict:
            if key == line[0]:
                id_dict[key] += float(line[3])

with open('salesreport.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Customer ID", "Total"])
    
    for key, value in id_dict.items():
        writer.writerow([key, value])
