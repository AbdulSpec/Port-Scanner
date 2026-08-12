PORT SCANNER

WHAT IT DOES:

The Port Scanner, scans ports’ in a range you have provided, it will return a list of results with what ports are open and which are closed, if it cannot connect to a port for any reason, whether that be Host failure, a filtered Port, or even just a timeout, it will return with “Failure to connect”, once it’s returned a list the code will log it into a back-up file for easier access.

WHY I BUILT IT:

The code was built with security in mind, ports represent one layer of a systems defence, auditing them is good security hygiene, open ports are more vulnerable to attacks, being able to identify which ports are closed/open are precautionary checks which mean is a port is open and investigation can be opened as to why and a sweep may be done.

HOW TO RUN IT:

Required Libraries:
No external libraries required

Running the code:
Change Start Port and End Port range in code.
What It Checks:
The code checks ports that are opened and ones that are closed, it then returns a list of which are open/closed.

TECHNOLOGIES USED:

Python 3 - Socket - Datetime

FUTURE IMPROVEMENTS:

Two major improvements the code could use, one being a shorter search span, for the time it takes to check which ports are open/closed, to do this threading could be implemented, threading simultaneously checks which ports are open rather than going through every code once at a time waiting for a result, the second major improvement being Server Identification, with what the server can do and what service it’s currently running on.
 with what the server can do and what service it’s currently running on.
