a={
    "Name" :  [" Ali, Owais, Hussain, Hadi, Anas"],
    "Age" :  [18, 22, 55, 24, 22],
    "Email" : ["Ali@gmail.com, Owais@gmail.com, Hussaingmail.com, Hadigmail.com, Anasgmail.com"]
}

#  Modifiction in current dictionary 
a  ["City"] = "karachi", "Birmingham, Hamburg"
a ["Country"] = "Pakistan", "United Kingdom, Germany"
# print(a)

# Remove a Specific key from the dictionary 

a.pop("Email")
# print(a)

# How to tell the user where is the error 

# print(a.get("Name", "Invalid Entry"), )
# print(a.get("Email", "Invalid Entry"), )

#  How do update the current dictionary ?

a.update(
    {
        "Phone" : "1234566",
        "Residence" : "Malir"
          })
print(a)
