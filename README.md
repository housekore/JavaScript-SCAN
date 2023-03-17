# JavaScript-Scanner
 Looking for sensitive data in .js links

# Phase One Enumerate .JS Files
Use other tools to enumerate .JS files for the domain in question.

For example, GetJS.

subfinder -d domain.com | anew > /home/kali/Subdomains/sud-domains.txt

cat domains.txt | getJS --complete -- verbose | anew >> /home/kali/Subdomains/r/js-domain.com.txt