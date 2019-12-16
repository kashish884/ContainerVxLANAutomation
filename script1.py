import sys
import os



def create_bridge(br):
    print("creating bridge {}".format(br))
    print(os.system("brctl addbr {}".format(br)))
    print(os.system("ip link set {} up".format(br)))

def vxlan_create(vx,vid,br):
    print("vxlan creation with {} {} {}".format(vx,vid,br))
    print(os.system("ip link add {} type vxlan id {} dstport 4789 local 192.168.10.2".format(vx,vid)))
    print(os.system("ip link set {} up".format(vx)))
    print(os.system("brctl addif {} {}".format(br,vx)))

def fdb_append(vx,dst):
    print("bridge fdb table appending with {} {}".format(vx,dst))
    print(os.system("bridge fdb append 00:00:00:00:00:00 dev {} dst {}".format(vx,dst)))


print("ENTER THE FOLLOWING!")

br = input("Bridge name for tenant: ")
vx = input("vxlan device name for tenant: ")
vid = input("vxlan id: ")
destin = input("destination endpoints (separate by commas)")

list_dst = destin.split(",")

create_bridge(br)
vxlan_create(vx,vid,br)

for each in list_dst:
    fdb_append(vx,each)

