mounths = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'Seteptember', 'October', 'November', 'December']
n =1 

while (n<4):
    mounth = int(input('Choose a mounth (1-12):' ))
    if 1 <= mounth < 13:
        print('The mounth is {}'.format(mounths[mounth-1]))
    n += 1