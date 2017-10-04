from nick import create_nick


with open('users.csv') as usersfile:
    for row in usersfile.readlines():
        user = row.strip().split(',')

        firstname = user[0]
        lastname = user[1]
        birthday = user[2]

        username = create_nick(firstname,lastname,birthday)

        #print out firstname, lastname and username

        nick = firstname + lastname + '=' + username
        print nick



