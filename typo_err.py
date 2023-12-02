import random


def generate_error(company_name):
    error_type = random.choice(["typo", "space", "punctuation"])
    
    if error_type == "typo":
        # Introduce a random typo in the company name
        index = random.randint(0, len(company_name) - 1)
        typo = random.choice(["S", "s", "m", "M", "K", "k", "L", "l", "t", "T"])
        company_name = company_name[:index] + typo + company_name[index + 1:]
    
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
    
    return company_name

# Original company name
original_name = "Smith Kline Ltd"

for _ in range(5):
    error_name = generate_error(original_name)
    print(error_name)
    
    
import random
import string

def random_letter_change(company_name):
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
    modified_name = company_name[:index_to_change] + replacement_letter + company_name[index_to_change + 1:]
    
    return modified_name

# Example company name
company_name = "Smith Kline Ltd"

# Generate a random letter change variation
modified_name = random_letter_change(company_name)

print(f"Original Company Name: {company_name}")
print(f"Modified Company Name: {modified_name}")