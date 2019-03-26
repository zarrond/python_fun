# -*- coding: utf-8 -*-
from debug_tools import dprint
import rsa
from rsa.key import PublicKey



(bob_pub, bob_priv) = rsa.newkeys(512)



with open("public.key",'w') as f:
    f.write(bob_pub.n.__str__()+'\n')
    f.write(bob_pub.e.__str__()+'\n')
print()

copy_bob_pub = None
with open("public.key","r") as f:
    n = int(f.readline())
    e = int(f.readline())
    copy_bob_pub = PublicKey(n,e)

print(bob_pub)
print(bob_priv)
#����� ��������� ��������� ���� � �������� ��� � UTF8, 
#��������� RSA �������� ������ � �������
message = 'hello Bob!'.encode('utf8')
print(message)
#����� ������� ��������� ��������� ������ ����
crypto = rsa.encrypt(message, copy_bob_pub)
print(crypto)
#��� �������������� ��������� ����� ��������� ������
message = rsa.decrypt(crypto, bob_priv)
print(message.decode('utf8'))