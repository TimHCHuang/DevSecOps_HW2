from yaml import *
f = open('mal.yml','r')
deserialized_data = unsafe_load(f)
print(deserialized_data)
