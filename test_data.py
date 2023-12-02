import random
import csv
from faker import Faker
import random
import string
from datetime import datetime

# Initialize Faker to generate random company and contact names
fake = Faker()

# Number of entries to generate
num_entries = 100  # Change this number as needed

# Create a list to store the generated data
data = []

max_number_orders=5

# Using locale dictionary to create faker locale generator    
local = {
        "United Kingdom": "en_GB",
        "France": "fr_FR",
        "Australia": "en_AU",
        "Netherlands": "nl_NL",
        "Germany": "de_DE",
        "Norway": "no_NO",
        "EIRE": "ga_IE",
    }
#CountryName = random.choice(list(local.keys()))
CountryName = "United Kingdom"

def get_random_date_after(after_date,plus_months):
        plus_string=f"+{plus_months}m"
        # Create errors in % of orders 
        #date_string = "2020-12-01"  # Example date and time format

        # Specify the format of the date string
        date_format = "%Y-%m-%d"

        # Parse the date string and convert it to a datetime object
        parsed_datetime = datetime.strptime(date_string, date_format)
        order_date = fake.date_between(start_date=after_date, end_date=plus_string)
        return order_date

# Function to convert the date string to the specified format
def convert_random_date_format(date_string):
    
    date_formats =  ["mm-dd-yyyy", "%Y-%m-%d", "%m-%d-%Y","%d %B %Y","%d %b %y"]
    #Add 27 enteries so that dates only changed in 1 in 30
    number_list=[number for number in range(1, 28)]
    date_formats= date_formats + number_list
    format_type = random.choice(date_formats)
    
    if format_type == "%m-%d-%Y":
        parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
        return parsed_date.strftime("%m-%d-%Y")
    elif format_type == "%d %B %Y":
        parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
        return parsed_date.strftime("%d %B %Y")
    elif format_type == "%d %b %y":
        parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
        return parsed_date.strftime("%d %b %y")

    return date_string
def generate_error(company_name):
    error_type = random.choice(["typo", "space", "punctuation","upper","lower","1","2","3","4","5","6","7","8","9","0","11","12"])
    
    if error_type == "typo":

        if len(company_name) < 2:
            return company_name  # Cannot change a letter if the name is too short
    
        # Choose a random index to change
        index_to_change = random.randint(0, len(company_name) - 1)
    
        # Get the letter at the chosen index
        original_letter = company_name[index_to_change]
    
        # Generate a random replacement letter
        replacement_letter = original_letter
    
        while replacement_letter == original_letter:
            replacement_letter = random.choice(string.ascii_letters)
    
        # Replace the letter in the company name
        company_name = company_name[:index_to_change] + replacement_letter + company_name[index_to_change + 1:]
    
    elif error_type == "space":
        # Add or remove a space in the company name
        if random.choice([True, False]):
            # Add a space
            index = random.randint(0, len(company_name))
            company_name = company_name[:index] + " " + company_name[index:]
        else:
            # Remove a space (if there's one)
            index = random.randint(0, len(company_name) - 1)
            if company_name[index] == " ":
                company_name = company_name[:index] + company_name[index + 1:]
    
    elif error_type == "punctuation":
        # Introduce a random punctuation error
        index = random.randint(0, len(company_name) - 1)
        punctuation = random.choice(["-", ".", ",", "&", "'", ""])
        company_name = company_name[:index] + punctuation + company_name[index:]
    
    elif error_type == "upper":
        company_name=company_name.upper()

    elif error_type == "lower":
        company_name=company_name.lower()

    return company_name

# Original company name
#original_name = "Smith Kline Ltd"

#for _ in range(5):
#    error_name = generate_error(original_name)
#    print(error_name)

code = local[CountryName]
fake = Faker(code)

# Generating fake data and adding it to dataframe
CustomerName = fake.name()
Address = fake.address()
Latitude = str(fake.latitude())
Longitude = str(fake.longitude())

# Generate random data for each entry
for _ in range(num_entries):
    order_date = fake.date_between()
    company_name = fake.company()
    contact_name = fake.name()
    order_status = random.choice(["Shipped", "Delivered", "Processing", "Completed"])

    data.append([order_date, company_name, contact_name, order_status])
    
    #sampled_items = random.sample(items, num_to_sample)

    num_orders=random.randint(1, max_number_orders)
    for i in range(num_orders):
        # Create errors in % of orders 
        date_string = "2020-12-01"  

        # Specify the format of the date string
        date_format = "%Y-%m-%d"

        # Parse the date string and convert it to a datetime object
        after_date = datetime.strptime(date_string, date_format)
        order_date=get_random_date_after(after_date,30)
        #company_name = fake.company()
        contact_name = fake.name()
        order_status = random.choice(["Shipped", "Delivered", "Processing", "Completed"])
        data.append([order_date, company_name, contact_name, order_status])
        order_company_name=generate_error(company_name)
        data.append([order_date, order_company_name, contact_name, order_status])
    
#Change the date format of 1 in 30 samples
for item in data:
        date_yyyy_dd=item[0].strftime("%Y-%m-%d")
        item[0]=convert_random_date_format(date_yyyy_dd)


#sampled_items = random.sample(data, 10)
#print(f"Sample=[{sampled_items}]")
    
# Define the CSV filename
csv_filename = "random_data.csv"

# Write the data to a CSV file
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["order_date", "company_name", "contact_name", "order_status"])  # Write header row
    writer.writerows(data)

print(f"Generated {num_entries} random entries and saved to {csv_filename}.")
