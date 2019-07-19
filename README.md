# clichat
Python chat for CLI

This chat is intended to be used over SSH connection solely in order to improve security. The following requirements below are strictly necessary for this application to work as it was intended to:

##### On the server machine
- Clone this repo onto your server machine (main target for the application to run).
- Make sure you manage correct access rights to the scripts.
- Create aliases for easier execution of the server.py and client.py scripts. (Check your bash, zsh, fish, etc) --> Usually "runserver" and "runclient" are used.
- Execute "runserver" on the server machine to start accepting connections from clients.

##### On the client machine
- Make sure you have ssh properly installed.
- Generate your keys with the script.
- Send your keys to the server with the script.
- 
