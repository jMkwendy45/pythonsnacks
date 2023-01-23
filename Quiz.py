input_str = input("Are you ready for these quiz,answer Yes/No: ")
if input_str == "No":
	print("Thank you please try again later!!!")
if input_str =="yes":

	questions = ['what is 0*2',"what is a noun","what is a verb",4*6,\
"what is the state capital of imo","Who is the Governor of lagos",8*9,"what is data",\
"What is the name of your insitution","how many states do we have in Nigeria ","what is the capital of cross river"\
"who is the football Goat","Who is your next president","which state do people spend their life on traffic"]

	answers =[0, "name of a person animal place or thing","a doing or action worst",\
"owerri","sanwo olu",58,"data is life","semicolon","36 states","Calabar","Messi","Peter obi","Lagos"]
if user_response == answer.index(question):
		print("Bravo!do you want to continue answer Yes/No: ")
if user_response != answers.__getitem__(i):
		print("you left quite on time!")


for i in range(len(questions)):
	

 for question in questions:
	user_response = input(f"{question}")




	


 