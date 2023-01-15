#!/usr/bin/python

# This is known as a shebang line due to the presence of the characters # and !. In unix based OS the program loader takes the presence of these two characters as an indication that the file is a script whereas the rest of the line specifies the interprter to be used for executing the cript  


try:
    import sys      #Used to take command line argumensts and exit when needed.
    import socket   #Used to test for valid URL
    import requests #Used to make HTTP requests and get responses.
    import pyfiglet
    from pyfiglet import Figlet

    rhost=sys.argv[1]    #rhost stands for remote host which is our target.
    wordlist=sys.argv[2]
    custom=Figlet(font="doom")
    print(custom.renderText("Dirbility")) #printing a custom ascii banner
    print("\n")
    #now we have to check whether the rhost or the target url is valid or not
    print("[*] Checking RHOST......")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # creating a socket to to make a test connection
    try:
        status=s.connect_ex((rhost,80)) # Using connect_ex method to connect to the URL.
        s.close()
        if (status==0):
            print (" [DONE] ")
            pass
        else:
            print (" [FAIL] ")
            print("[!] Error: Cannot reach RHOST %s/n" %(rhost))
            sys.exit(1)
    except socket.error:
        print (" [FAIL] ")
        print("[!] Error: Cannot reach RHOST %s/n" %(rhost))
        sys.exit(1)

    #now we move on to reading the wordlist

    print ("[*] Parsing Wordlist.......")
    try:
        with open(wordlist) as file:
            to_check=file.read().strip().split('\n') # we used .read() function to get the contents, .strip() fuction to get rid of the extra newline at the end of each file and the .split() function to use the newline character as the split marker
        print("[DONE]")
        print("[*] Total paths to check: %s" %(str(len(to_check)))) 
    except IOError:
        print ("[FAIL]")
        print("[!] Error: Failed to load the specified file\n")
        sys.exit(1)

#Now we will make the path checking function
    def checkpath(path):
        try:
            response=requests.get("http://"+rhost+"/"+path).status_code #making the request
        except Exception:
            print("[!] Error: An unexpected eeror occured ")
            sys.exit(1)
        if (response==200):
            print(" [*] Valid path found: %s" %(path))

    #Iterating over the list of paths
    print ("\n [*] Beginning Scan....\n")
    for i in range (len(to_check)):
        checkpath(to_check[i])
    print ("\n [*] Scan Complete! ")


except KeyboardInterrupt:
    print ("\n [!] Error! User Interrupted Scan")
    sys.exit(1)




