
import re
def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$",  email ))


a  =valid_email('trsasa@gmail.com')
print(a)

