import os


def main(): 
    title()
    
    dir = input(' Write directory to set folder setup: ')
    name = input('Name of the main folder: ').replace(os.path.sep, '\\')
    os.chdir(dir)
    
    os.mkdir(name)
    
    os.chdir(dir+'\\'+name)
    
    os.mkdir('Raw data')
    os.mkdir('Code')
    os.mkdir('Processed data')
    os.mkdir('Results')

    with open('readme.md','w') as f:
        f.write('Insert Read me file information')
        
    input('Folder setud done! Press space to continue')




def title():
    print('''
 _____ ____  _     ____  _____ ____   
/    //  _ \/ \   /  _ \/  __//  __\  
|  __\| / \|| |   | | \||  \  |  \/|  
| |   | \_/|| |_/\| |_/||  /_ |    /  
\_/   \____/\____/\____/\____\\_/\_\  
                                      
 ____  _____ _____  _     ____        
/ ___\/  __//__ __\/ \ /\/  __\       
|    \|  \    / \  | | |||  \/|       
\___ ||  /_   | |  | \_/||  __/       
\____/\____\  \_/  \____/\_/  

####################################
        
''')


if __name__ == '__main__':
    main()
    
    