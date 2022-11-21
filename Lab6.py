#1a
text = "Python uses whitesapce indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements. It's a sign that the current block will end if the indentation decreases. Thus, the program's visual structure accurately represents its semantic structue. The recommended indent size is four spaces."
"visual" in text
#True
#1b
"Visual" in text
#False
#1c
"program" in text
#True
#1d
"accur" in text
#True
#2
name = input("Enter your first name: ")
lastname = input("Enter your last name: ")
age = input("Enter your age in numerical form: ")

print(f"Hello {name} {lastname}, are you {age} years old?")
print("Hello " + name + " " + lastname + ", are you " + age + " years old?")
print("Hello %s %s, are you %s years old?" % (name, lastname, age))

#3
current_year = 2022
birth_year = current_year - int(age)

print(
  f"Hello, {name} {lastname}, are you {age} years old? Were you born in {birth_year}?"
)
#4
import pyinputplus as pyip

response = pyip.inputAddress

birth_month = pyip.inputNum("Please enter the Month that you were born: ")
#When i enter blank values and "November" i get the message "blank values are not allowed" and "November is not a number". When i input 11 and 11.5 the programs output is 11 and 11.5.

#5a
birth_month = pyip.inputInt("Enter your birth month as an integer: ")

#it accepts 11 and nothing happens afterward, it returns the message "11.5 is not an integer" for 11.5, the program would accept 1111 and not return anything.
#5b
birth_month = pyip.inputInt("Enter your birth month as a two-digit number: ",
                            min=1,
                            max=12)
#the script accepts 1 and 12 and doesn't return any message, but when i say 13 i get the message "number must be at maximum 12"
#5c
while True:
  birth_year = pyip.inputInt("Enter your birth year with four digits: ")
  if len(str(birth_year)) != 4:
    print("Must be four characters")
    continue
  elif len(str(birth_year)) == 4:
    print(birth_year)
    break
#when i entered 98 originally it would accept the value, but after the rule i wrote it will return the message "must be four characters". '98 returns the message "'98 is not an integer" and 1998 is accepted.
