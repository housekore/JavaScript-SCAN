# JS-SCAN
 Looking for sensitive data in .js links

# Phase One Enumerate Subdomains and .js links
* 1 - Use a tool, for example <a href="https://github.com/projectdiscovery/subfinder" target="_blank">SubFinder</a> to enumarate all subdomains 
* 2-  Use a tool, for example <a href="https://github.com/003random/getJS" target="_blank">GetJS</a> to enumarete all .JS links.

# Phase Two - Configure findsecrets.py
## With a list of links in .JS, it's time to use the tool.
* On line 10 we have the configuration of the directory where your files with a .JS link are located.*
* On line 11 we have the configuration of your file with regular expressions (Regex).*

![Path](https://github.com/housekore/JavaScript-SCAN/blob/main/images/image01.png)

# Phase Tree - Init the Script
* Enter the script folder + file with .JS links and run the script.*

`python3 findsecrets.py`

* An alphabetical menu will be presented, where you must select the file to run the tests.*
* If it finds any parameter based on the regular expression of the regex.txt file (or configured file) it will be informed on the screen.*
* Results are saved in the same folder for further analysis.*

![Path](https://github.com/housekore/JavaScript-SCAN/blob/main/images/Image02.png)

# What search on .JS links?

### Here are some advantages of bug bounty/bug hunting for sensitive information like API keys and other data in .js files:

* Increased security: By identifying and reporting sensitive information in .js files, security vulnerabilities can be addressed before they are exploited by malicious actors, leading to improved overall security.* 
* Reduced risk of data breaches: By identifying and mitigating security vulnerabilities, bug bounty/bug hunting can help reduce the risk of data breaches, which can be costly and damaging to an organization.*
* Rewarding: Bug bounty programs offer rewards for identifying and reporting security vulnerabilities, making it an attractive option for security researchers and hackers. *
* Helps organizations stay compliant: By identifying sensitive information in .js files, organizations can ensure they are meeting regulatory and compliance requirements, such as GDPR and LGPD.*
* Improves reputation: By taking proactive steps to identify and address security vulnerabilities, organizations can improve their reputation and build trust with their customers and stakeholders.*

# Support
You can Follow me on <a href="https://www.linkedin.com/in/jose-jardel-lgpd-cybersecurity/" target="_blank">Linkedin</a> or

<a href="https://www.buymeacoffee.com/jjardel"><img src="https://github.com/housekore/JavaScript-SCAN/blob/main/images/buy-coffe.png" alt="jjardel-imagem" width="25%"></a>

