import random

# List of common Indian first names (feel free to modify or expand)
first_names_male = [
    "Abhijeet", "Abhishek", "Ajay", "Akash", "Amit", "Arjun", "Ashish", "Ayush", 
    "Chandrashekhar", "Dhruv", "Gaurav", "Harsh", "Rahul", "Rohan", "Sagar", "Sahil", 
    "Sandeep", "Shubham", "Siddhार्थ", "Sohan", "Vikram", "Yash"
]

first_names_female = [
    "Aarti", "Anjali", "Deepika", "Diya", "Hiya", "Isha", "Kiara", "Kriti", 
    "Manisha", "Neha", "Priya", "Pooja", "Riya", "Rani", "Sonia", "Tanya", 
    "Trisha", "Urvashi", "Vaani", "Zoya"
]

last_names = [
    "Kumar", "Singh", "Patel", "Das", "Sharma", "Rao", "Gupta", "Mehta", 
    "Kaur", "Pandey", "Yadav", "Joshi", "Trivedi", "Verma", "Mittal", "Shah", 
    "Bose", "Nair", "Reddy"
]

# Function to generate a random full name
def generate_name(male=True):
  first_names = first_names_male if male else first_names_female
  return random.choice(first_names) + " " + random.choice(last_names)

# Generate 309 random names (adjust the number as needed)
names = set()

while len(names) <= 309:
  names.add(generate_name(male=random.randint(0,1)))

# Print or copy the names (modify for your needs)
for name in names:
  print(name)  # This will print each name on a new line
  # You can modify this loop to directly write the names to a file or clipboard
