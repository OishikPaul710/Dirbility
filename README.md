# Dirbility
A directory brute forcing tool that like the name suggests brute force  directory locations based on HTTP response codes.

When speaking with a web server, a variety of HTTP response codes are employed. However, only 200 and 404 matter to us for now. When a legitimate page or directory is requested, the 200 (OK) code is used. The 404 error code is most likely already familiar to you. When a requested page or directory doesn't exist, it is utilised.
In order to determine whether we can traverse to this recently discovered directory, we can issue queries for potential directories and then examine the answer.

Process to run:


1.Create a wordlist in the root folder of your host machine (as shown below)

![image](https://user-images.githubusercontent.com/88844855/212553484-d7b9fe3f-4b80-4a49-9286-9536baae9419.png)


2. Run the script dirbility.py in the following format (as shown below)

![image](https://user-images.githubusercontent.com/88844855/212553553-d008c02a-5e50-462b-8636-08f9460f787a.png)

NOTE: Run the script from the folder you have saved the script in.


3. The results will be displayed on the screen (as shown below)

![image](https://user-images.githubusercontent.com/88844855/212553632-2aa7ec69-8fe3-4330-a1d8-5c72f4c59e1d.png)


