import os
c = input("Choose your environment: [0] pip / [1] pip3 : ")

if c == "0":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pystyle")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install icmplib")
    os.system("pip install dnspython")
    os.system("pip install httpx")
    os.system("pip install undetected_chromedriver")
    os.system("pip install shutup")
    os.system("pip install psutil")
    os.system("pip install flask")
    os.system("pip install winreg")
elif c == "1":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pystyle")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install requests")
    os.system("pip3 install icmplib")
    os.system("pip3 install dnspython")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
    os.system("pip3 install shutup")
    os.system("pip3 install psutil")
    os.system("pip3 install flask")
    os.system("pip3 install winreg")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")
