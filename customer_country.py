def process_customer_data(input_file, output_file):
    with open(input_file, 'r') as file:
        header = file.readline().strip().split(",")
        first_name_index = header.index("FirstName")
        last_name_index = header.index("LastName")
        country_index = header.index("Country")
        
        data = []
        for line in file:
            values = line.strip().split(",")
            data.append([values[first_name_index], values[last_name_index], values[country_index]])
    
    with open(output_file, 'w') as file:
        total_employees = len(data)
        file.write(f"Total Employees: {total_employees}\n")
        file.write("FirstName,LastName,Country\n")
        for item in data:
            file.write(f"{item[0]},{item[1]},{item[2]}\n")

input_file = "customers.csv"
output_file = "customer_country.csv"

process_customer_data(input_file, output_file)