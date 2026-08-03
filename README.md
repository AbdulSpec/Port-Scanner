Port Scanner


What It Does:
The Port Scanner once run, scans ports’ in a range you have provided, for example, range given: 79-85, the port scanner will scan only the ports between the start port, 79, and the end port, 85, it will return with a list of results with what ports are open and which are closed, if it cannot connect to a port for any reason, whether that be Host failure, a filtered Port, or even just a timeout, it will return with a “Failure to connect”, once it’s returned a list the code will log it into a back-up file for easier access.
Why I Built It:
The code was built with security in mind, ports represent one layer of a systems defence, auditing them is good security hygiene, open ports are more vulnerable to attacks, being able to identify which ports are closed/open are precautionary checks which mean is a port is open and investigation can be opened as to why and a sweep may be done.
How To Run It:
Required Libraries:
No external libraries required

Running the code:
Change Start Port and End Port range in code.
What It Checks:
The code checks ports that are opened and ones that are closed, it then returns a list of which are open/closed.
Technologies Used:
Python 3
Socket
Datetime
Future Improvements:
Two major improvements the code could use, one being a shorter search span, for the time it takes to check which ports are open/closed, to do this threading could be implemented, threading simultaneously checks which ports are open rather than going through every code once at a time waiting for a result, the second major improvement being Server Identification, with what the server can do and what service it’s currently running on.
