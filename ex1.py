import re

text = "helo team ,our new peoduct is planned for 25/05/2026 at 10.30 A.M. Please contact marketing.team@startupAI.com or support@startupAI.com for more details. Follow us on social media using #startupAI #productlaunch. the earlr-bird price is 2999$(limited offer!!) and valid for 100 users only.https://google.com."

hashtags = re.findall(r"#\w+", text)
mentions = re.findall(r"@\w+", text)
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
dates = re.findall(r"\b\d{1,2}/\d{1,2}/\d{4}\b", text)
url = re.findall(r"https?://\S+", text)
tokens = re.findall(r"\b\w+\b", text)

print("hashtags:", hashtags)
print("mentions:", mentions)
print("dates:", dates)
print("emails:", emails)
print("url:", url)
print("tokens:", tokens)

