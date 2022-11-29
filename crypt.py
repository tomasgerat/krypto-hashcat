
from hashlib import md5
from base64 import b64encode

def crypt( passwd, salt ):
  m = md5()
  m.update( passwd )
  m.update( salt )
  return b64encode( m.digest() )
  
print crypt( 'heslo', '02SK64Xv')
