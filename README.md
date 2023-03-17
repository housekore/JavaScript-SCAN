# JavaScript-SCAN
 Looking for sensitive data in .js links

# Phase One Enumerate .JS Files
Use other tools to enumerate .JS files for the domain in question.

For example, <a href="https://github.com/003random/getJS" target="_blank">GetJS</a>

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

# Support
You can Follow me on <a href="https://www.linkedin.com/in/jose-jardel-lgpd-cybersecurity/" target="_blank">GetJS</a> or

<a href="https://www.buymeacoffee.com/jjardel"><img src="https://github.com/housekore/JavaScript-SCAN/blob/main/images/buy-coffe.png" alt="jjardel-imagem" width="25%"></a>

