#make the list of the invited people 
names = ['joe' , 'micheal' , 'zamir' , 'munzir' , 'jimmy']

#change the name of the person can't come
n_coming = names.pop(1) #(n_coming means that "not coming")
names.append('randy')
#make a message for inviting the people 
message = f"How are you doing, hope you're fine I just wanted to \ninvite you into a dinner party tonight \n my lovely: \n"

#print the message for coming people 
print(f"{message}{names[0].title()}.\n\n" , f"{message}{names[1].title()}.\n\n", f"{message}{names[2].title()}.\n\n", f"{message}{names[3].title()}.\n\n", f"{message}{names[4].title()}.\n\n")

#print the name of the person who can't make it
print(f"{n_coming.title()} can't make it")
