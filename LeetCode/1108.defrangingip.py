# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

 

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

 

# Constraints:

#     The given address is a valid IPv4 address.


class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = 0
        while(i < len(address)):
            if address[i] == '.':
                address = address[:i]+'[.]'+address[i+1:]
                i+=2
            else:
                i+=1
        return address

