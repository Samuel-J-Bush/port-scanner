# Port scanner
Simple python port scanner that uses TCP sockets to create network communication endpoints and determine if any ports are open.

## Checked ports
- A single IP address on a devce can have 65,535 different ports for network communication.
- This program checks the common ports that are targeted which haved been stored in a dictionary.
- The dictionary defines 19, but can be adapted by changing only the dictionary.
- To do this, update dictionary with the port and service. The rest of the logic is the same.

## TCP (Transmission control protocol) sockets
- The TCP socket creates a reliable, bidirectional connection for data transfer.
- The source port number, target port number, source IP and target IP are all used in TCP sockets.
- The source port is ephemeral and the target port is iterared.

## Output
- If/when ports are found to be open, theyre assigned to another dictionary/
- This is then outputted containing only the open ports.
- If no ports are open, the program simply responds stating this.

## Important
Scanning devices or sites unauthorised is illegal, even if no data is accessed or no damage to target.
