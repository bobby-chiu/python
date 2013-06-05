# Filename: run_addressbook.py


from person import person
import os,sys
import cPickle as p



def info_input():
    name = raw_input('Enter name:')
    address = raw_input('Enter address:')
    group = raw_input('Enter group:')
    persontuple = (name,address,group)
    persondict = person(persontuple)

    return persondict

def read_address(filename):
    f = file(filename,'r')
    addresslist = p.load(f)
    f.close()
    return addresslist

def write_address(filename,lst):
    f = file(filename,'w')
    p.dump(lst,f)
    f.close()

addressfile = r'.\addressBook'
addressdict = {}
helpinfo = "Hello,this is an address book software,\n\
To use it, you should specify the argument among the following five arguments.\n\
    --add(--a):add a new contact person into addressbook\n\
    --update(--u):update the info you specified of an existing person\n\
    --delete(--d):delete the person info of an existing person\n\
    --search(--s):search and list contact person\n\
    --help(--h):show this help info\n \n"


#if len(sys.argv) < 2:
#   print 'error:too less arguments.you can use --help(--h) to get more infomation for using this program'
#   print 'please restart this program with argument'
#   sys.exit(1)
#
if not os.path.exists(addressfile):
    '''check if there exist the addressBook file'''

    print 'The addressBook now is uncreated\n\
please add the new contract person first.\n\
Do you want to add(press "y") person or exit(press "n" or any other chars):'
    choose = raw_input()
    if choose == "y":
        pA = info_input()
        flag = pA.add_person(addressdict)
        write_address(addressfile,addressdict)
        if flag != False:
            print 'addressBook created successfully.'
    else:
        print 'Jesus'
        sys.exist(1)

while True:
    print 'please assign the argument you want to operate,\nor you can use --help(--h) for help:'
    option = raw_input()
    if option.startswith("--"):
        option = option[2:]
        addressdict = read_address(addressfile)
    elif option == '':
        continue
    else:
        print 'error: argument invalid synax,you can use --help(--h) to get more infomation'
        continue

    if option == "help" or option == "h":
        print helpinfo

    elif option == "add" or option == "a":
        print 'Enter the person you want to add:'
        pA = info_input()
        flag = pA.add_person(addressdict)
        write_address(addressfile,addressdict)
        if flag != False:
            print 'addressBook added successfully.'

    elif option == "update" or option == "u":
        print 'Enter the person you want to update:'
        pU = info_input()
        flag = pU.update_person(addressdict)
        write_address(addressfile,addressdict)
        if flag != False:
            print 'addressBook updated successfully.'


    elif option == "delete" or option == "d":
        print 'Enter the person <name> you want to delete:'
        name = raw_input()
        persontuple = (name,'','')
        pD = person(persontuple)
        flag = pD.delete_person(addressdict)
        write_address(addressfile,addressdict)
        if flag != False:
            print 'addressBook person %s delete successfully.' % name

    elif option == "search" or option == "s":
        print 'Enter the person <name> you want to search:'
        name = raw_input()
        if name != '':
            persontuple = (name,'','')
            pS = person(persontuple)
            personInfo = pS.search_person(addressdict)
            if personInfo != False:
                print '%s\'s information is (address,group):%s' % (name,personInfo)
        else:
            print 'addressBook list now is:\n',
            for key in addressdict.keys():
                print '%s\'s information is (address,group):%s' % (key,addressdict[key])

    else:
        print 'error: argument invalid synax,you can use --help(--h) to get more infomation'
        continue
    while True:
        print 'Do you want to continue("y") this program or exit("n"):'
        op = raw_input()
        if op == "y":
            break
        elif op == "n":
            sys.exit(1)
        elif op == '':
            continue
        else:
            print 'invalid input'

