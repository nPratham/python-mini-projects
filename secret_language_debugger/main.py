# Text coder and Decoder
def coding(code):
# Split the input text into a list of words
    list1 = code.split()
    for index in range(len(list1)):
            i = list1[index]
            if len(i)>= 3: # If the word has 3 or more characters, apply the custom transformation
                list1[index] = i[2]+i[0]+i[1] + i[-1] + i[1:-1]+i[0] + i[0:3]
            else:
                list1[index] = i[::-1] # For words shorter than 3 characters, just reverse them
    updated_text = " ".join(list1)# Join the transformed list back into a string
    print(updated_text)

# Function to decode (or "debug") the previously encoded text       
def debugging(bad_text):
    list2 = bad_text.split()  # Split the encoded text into words
    for index in range(len(list2)):
          i = list2[index]
          if len(i)>= 3: # If the word has 3 or more characters, reverse the transformation
            main = i[3:-3]
            list2[index] = main[-1] + main[1:-1]+main[0]
          else: # Reverse short words 
            list2[index] = i[::-1]
    updated_text2 = " ".join(list2) # Join the decoded list back into a string
    print(updated_text2)

# Main control flow
# Ask user to select an option 
#          
option_selected = input("Do You want to debug or code , Please Select valid option: ")
if option_selected == 'debug':
    user_debug_code = input("Enter text which you want to debug: ")
    debugging(user_debug_code)
elif option_selected == 'code':
    user_code = input("Enter your text for conversion: ")
    coding(user_code)
else: # Handle invalid option
    print("please check valid option") 
