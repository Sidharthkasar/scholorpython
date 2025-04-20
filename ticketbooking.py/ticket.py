# remove funticon

tkts=[1,2,3,4,5]
print('available tickets:', tkts)
user_input= int(input('Enter how many tickets you want to book:'))
for x in range(user_input):
    ticket_num=int(input('Enter ticket number:'))
    tkts.remove(ticket_num) # remove() method removes the first occurence of the element with the specified value
print('available tickets:', tkts)
