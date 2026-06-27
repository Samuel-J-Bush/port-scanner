import socket 

common_ports = { 
  21: 'FTP',
  22: 'SSH',
  23: 'Telnet',
  25: 'SMTP',
  80: 'HTTP',
  110: 'POP3',
  139: 'NetBIOS'
  143: 'IMAP',
  443: 'HTTPS',
  445: 'SMB',
  1883: 'MQTT'
  3306: 'MySQL',
  3389: 'RDP',
  5432: 'PostgreSQL',
  6379: 'Redis'
  8080: 'HTTP-Alt',
  8443: 'HTTPS-Alt',
  9200: 'Elasticsearch',
  27017: 'MongoDB'
} # Dictionary for the commonly targeted ports


def portscanner(target,port): # Function for checking induvidual ports
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket for connecting to the port 
    
    sock.settimeout(1) # Allow 1 second to connect to the port
    result = sock.connect_ex((target,port)) # Try to connect to the port of the target - if successful the result = 0
    sock.close() # Close the socket after attempting to connect to the port

    if result == 0: # If result is 0 port is open
      return True
    else: # Else if result isnt 0 port is closed
      return False
  except socket.error: # If there is an error treat the port as being closed
    return False


target = input("Enter the target domain or target IP: ") # User enters the target for the port scanner
try:
  validateip = socket.gethostbyname(target) # Attempts to validate the target
except socket.gaierror: # Target is not validated
  print("Error - target cannot be validated - maybe check input")
  exit(1) # Ends the whole program as target is not valid
  
openports = [] # List that will be appended with any ports that are open
print(f"Scanning {target} in progress")

counter = 0
for port, service in common_ports.items(): # To check every port in the port dictionary
  counter += 1
  print(f"Scanning {counter} of {len(commmon_ports)}")
  if portscanner(target, port): # Checks if the function returns True or False - open or closed
    openports.append((port, service)) # Adds the name of the open port to the open ports list
    print(f"{port}: {service} is open") # Lets user know straight away if open port is found


print(f"Scan of {target} is complete") 
if len(openports) > 0:
  print("Here are the open port(s):")
  print(openports) # Only prints list if it contains names of open ports
else:
  print("None of the scanned ports were open")