# Hi, I'm Dr4ks! 👋

## 🚀 About Me
I'm a Cyber Security student and open always to learning.

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/Dr4ks/)
[![hackerrank](https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white)](https://www.hackerrank.com/Dr4ks)
[![tryhackme](https://img.shields.io/badge/tryhackme-1DB954?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/Dr4ks)
[![HackTheBox](https://img.shields.io/badge/HackTheBox-2DC3E8?style=for-the-badge&logo=hackthebox&logoColor=green)](https://app.hackthebox.com/profile/1037035)
[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dr4ks)


# Secret Santa Phishing
This repository is created to make Phishing for workers of any company by cheating people via **Secret Santa** game which happening in New Year eve.

# How Phishing works for victim and attacker

1. Victim reads [Email](email.md) coming from his coworker.
2. Victim trusts the link as coming from his coworker and opens a link, add Domain credentials to form without checking company's asset database that such service is valid or non-valid.
3. Attacker sets up web application by running `py script.py` on his attacker machine and waits for victims.
4. Once, victim enter his or her Domain credentials, attacker can see grabbed credentials in this [file](results/success.txt).

**Reminder!** I build regex for username and password fields due to a company's policy, you can also change. <br />

**Purpose of regex's usecase** is to imitate web application as connected to Domain via LDAP. As a result, victim can trust. <br />
If victim doesn't trust to attacker's web application and enters invalid credentials , it can also be seen on this [file](results/fail.txt)


# Phishing Scenario
![Video](example.gif)


