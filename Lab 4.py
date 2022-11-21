#!/usr/bin/env python
# coding: utf-8

# In[76]:


#1

active_program=["read the textbook", "practice the textbook", "Google questions", "watch videos", 
                 "go to class", "go to office hours", "work with friends", "do the homework"]
print(active_program)

print(active_program[0])
print(active_program[:3])
print(active_program[3:])

active_program.append("look at tutorials")
print(active_program)
active_program.append("watch movies about programmers")
print(active_program)

active_program.insert(0, "desire to learn")
active_program.insert(1, "commitment to learning")
print(active_program)

active_program[10]="watch tutorials online"
print(active_program)
active_program.remove("watch movies about programmers")
print(active_program)

del active_program[0]
print(active_program)

most_relevant_action = active_program.pop(2)
print(most_relevant_action)

active_program.insert(0,"practice the textbook")
print(active_program)

print(active_program[0:3])

active_program_2 = active_program
print(active_program_2)

del active_program_2[2]
del active_program_2[3]
active_program_2.remove("Google questions")
active_program_2.remove("go to class")
active_program_2.remove("work with friends")
print(active_program_2)

"commitment to learning" in active_program_2


# In[2]:


#2
active_program = ["read the textbook", "practice the textbook", "Google questions", "watch videos", 
                 "go to class", "go to office hours", "work with friends", "do the homework"]
active_program_2 = ['practice the textbook', 'commitment to learning', 
                    'go to office hours', 'do the homework', 'watch tutorials online']
 
for x in active_program_2:
    print("Every other day, I will " + x + " to become a better programmer")
   
for x in active_program_2[0:1]:
    print("Every day, I will " + x + " to become a better programmer")
    

for x in active_program[3:]:
        print("Every week, I could " + x + " to become a better programmer.")
    


# In[42]:


#3

list_id = [100,108,124,131,171,197]
list_name = ["Information in the 21st Century", "Programming for Problem Solving", "Cybersecurity Basics", "Introduction to Data Analytics", "eSports & Digital Gaming Ecosystem", "Mini Special Topic in Informatics"]

list_id.sort()
print(list_id)

list_name.sort()
print(list_name)

list_id.sort(reverse=True)
print(list_id)

list_name.sort(reverse=True)
print(list_name)

#cannot unsort, but if you want to you could use a tuple since it's immutable



course_name = zip(list_id, list_name)
for id, name in course_name:
    print(id, " ", name)



# In[37]:


#4

course_id_t = ("100", "108", "124", "171", "197")
course_name_t = ("Information in the 21st Century", "Programming for Problem Solving", "Cybersecurity Basics", "Introduction to Data Analytics", "eSports & Digital Gaming Ecosystem", "Mini Special Topic in Informatics")

print("Welcome to CINF " + str(course_id_t[0]) + " " + course_name_t[0] + "!")

#cannot append tuples

#cannot change tuples

course = zip(course_id_t, course_name_t)


for id, name in course:
    print(id," ", name)


# In[ ]:





# In[ ]:




