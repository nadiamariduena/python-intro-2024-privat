### 👾 Network protocols


🟧 When looking for the definition and purpose of the **bitwise operators**  ➡️ [z_Bitwise_operator.md](../z_Bitwise_operator.md) , I found that they can be used in network protocols. Since I am just starting with Python and am not yet familiar with these concepts, I will save this information for future reference.



<br>
<br>

 Network protocols often use **bitwise** operations to manage and interpret data efficiently. One classic example is the TCP/IP protocol suite, particularly in the IP header and TCP flags. Let’s explore an example related to the TCP header flags to illustrate how bitwise operations are used


 <br>

## TCP Header Flags Example


<br>

[TCP IP Model Explained | TCP IP Model Animation | TCP IP Protocol Suite | TCP IP Layers | TechTerms](https://youtu.be/2QGgEk20RXM?si=sAkIE2gspgAomxFi)


In **TCP** (**Transmission Control Protocol**), the **header** contains a set of flags that control the state and behavior of the TCP connection. These flags are represented as individual bits in a 6-bit field within the TCP header.

#### The flags are:

```bash
URG (Urgent Pointer field significant)
ACK (Acknowledgment field significant)
PSH (Push Function)
RST (Reset the connection)
SYN (Synchronize sequence numbers)
FIN (No more data from the sender)
```


