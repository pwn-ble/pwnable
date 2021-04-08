

John the ripper or JTR

Two main types of brute forcing

1) Dictionary attack

2) Brute forcing attacks


Dictionary attacks utilize .lst (list) files to crack the password and is less resource and time consuming, but requires some knowledge of your target


Bruteforce attacks attempt to crack the password by trying every "possible" password


you utilize the command as follows:

john -wordlist=password.lst hashfile

*where the "password.lst" file is the file where you either obtained, or developed your own word combonations
for cracking purposes.


The user can develop their own password lists using the command crunch

..
