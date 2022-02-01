# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True 
}
user2 = {
    'name': 'pepe',
    'valid': True
}

def authenticated(fn):
    def wrapf(*args,**kargs):
        if args[0]['valid']:
            return fn(*args,**kargs)
    return wrapf

@authenticated
def message_friends(*user):
    name = user[0]['name']
    print(f'message has been sent from: {name}')

message_friends(user1,user2)
message_friends(user2,user1)