from Rele_lib import Relay, RelayNC, RelayNO, RelaySSR

# test code
RelayOne = RelaySSR("rele", 0,)


print(RelayOne.get_state())

RelayOne.start()
print(RelayOne.get_state())

RelayOne.stop()
print(RelayOne.get_state())

print(RelayOne.get_info())
