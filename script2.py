
import os
import sys

def add_vm(br, veth):
    print(os.system("brctl addif {} {}".format(br,veth)))


br = input("Bridge name of the tenant: ")
veth = input("veth that has the desired vm on the other end: ")

add_vm(br,veth)