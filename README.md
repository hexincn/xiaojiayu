转载..。。。。。
MS17-010

由于我们所有的研究现在都在Metasploit的主存储库中，所以没有任何理由会让每个人都把这个存储库打开，因为有两个版本的一切，由于压倒性的人气支持成为一个噩梦，因为这只是一个侧面的项目。请不要在这里提出支持问题，因为他们不会回答。

寻找扫描仪的人：

Metasploit：https：//www.rapid7.com/db/modules/auxiliary/scanner/smb/smb_ms17_010
Python：https：//github.com/nixawk/labs/blob/master/MS17_010/smb_exploit.py
寻找永恒之蓝的人：

https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue
https://community.rapid7.com/community/metasploit/blog/2017/05/17/metasploit-the-power-of-the-community-and-eternalblue
此版本反驳了大多数现有IDS规则（当时）的稳健性。那些想做IDS规则的人应该看看最终的SMB1 Trans2数据包。这些包含固定的偏移量，但可能使用其他地址。然而，这些偏移位置的孔必须总是以类似的方式布置。还有许多其他模式，例如具有空标题和shellcode的几个SMB2新郎请求以及“空洞”会话设置。

Windows内核shellcode将在Metasploit中，并在x86版本完成时提交到exploit-db。
