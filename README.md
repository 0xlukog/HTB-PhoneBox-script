# HTB-PhoneBox-script
This script is used to obtain a flag in Hack The Box CTF challenge.
The challenge can be found www.hackthebox.eu

When you press "Start" they will provide you an instance ip:port.
We will find a vulnerability to exploit, if you enter "*" as username and "*" as password, you can bypass the login, but with this you still won't be able to get the flag.

This script takes advantage of this vulnerability by loading as a payload each character with "*" in each field until access is achieved, decoding the user and password 
(this will be the flag :) ).

Dont forget to change your instance ip in the script file.
