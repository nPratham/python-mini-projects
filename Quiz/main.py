list1 = ['What is the capital city of Australia?','Which planet is known as the Red Planet?','What is the smallest prime number?'
,'Who wrote "Romeo and Juliet"?','What is the largest mammal?']
list2 = ['canberra','mars','2','william shakespeare','blue whale']
number = 0
reward = 0

for i in list1:
    print(f"the question is: {i} ")
    answer1 = input("Enter you answer: ")
    if answer1 == list2[number]:
        reward += 100
        print(f"this answer is correct! and reward is {reward}")
        number+=1
    else:
        print("Wrong Answer!")
        break

print(f"you won ${reward}")


