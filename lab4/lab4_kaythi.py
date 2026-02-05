"""
Soe Kaythi
Feb 5, 2026
Lab 4, Dictionary
"""

print("\n---Example 1: Dictionary---")
# declare and initialize a dictionary
contacts = {
    "Bill Gates": "917-555-1234",
    "Jane Smith": "718-555-5678",
    "Emily Davis": "718-555-8765"
}
print(f"Original contacts: {contacts}")

# update an existing contact
contacts["Jane Smith"] = "718-555-9999"
print(f"Updated contacts: {contacts}")

# add a new contact
contacts["Peter Parker"] = "718-555-4321"
print(f"Contacts after adding new contact: {contacts}")

# loop through the dictionary
print("\n---Example 2: Looping through a Dictionary---")

for v in contacts:
    print(v) # v is the key value

for v in contacts:
    print(contacts[v]) # print the corresponding value

for v in contacts:
    print(f"{v}: Phone Number: {contacts[v]}") # print both key and value

print("\n---Example 3: items(),keys(),values() Method---\n")
# items method return all the key-value pairs
print(f"items in the dictionary: {contacts.items()}\n")
# keys method returns all the keys in the dictionary
print(f"keys in the dictionary: {contacts.keys()}\n")
# values method returns all the values in the dictionary
print(f"values in the dictionary: {contacts.values()}\n")

print("\n---Example 4: checking for existence of a key---\n")
# check if a key exists in the dictionary
check_name = "Emily Davis"
check = check_name in contacts
print(f"Is {check_name} in contacts? {check}")

print("\n---Example 5: Length of the dictionary---\n")
# get the length of the dictionary
print(f"Number of contacts: {len(contacts)}")

print("\n---Example 6: Deleting a key-value pair---\n")
# delete a key-value pair
print(f"Contacts: {contacts}")
contacts.pop("Bill Gates")
print(f"Updated contacts: {contacts}")

print("\n---Example 7: get Method---\n")
# get method returns the key-value pair
print(f"Emily Davis's phone number is: {contacts.get('Emily Davis')}")

print("\n---Example 8: update Method---\n")
# update method updates the key-value pair
contacts.update({"Emily Davis": "718-888-0000"})
print(f"Updated contacts: {contacts}")

print("\n---Exercise---\n")