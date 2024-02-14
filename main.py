from Relay_lib import Relay, RelayNC, RelaySSR


# test code

rele_coil = 0
rele_state = 0

RelayOne = RelayNC("rele", rele_state)

print(RelayOne.get_state())

rele_coil = RelayOne.start()
# simulace fyzickeho rele
if rele_coil == 1:
    RelayOne.state = 1
print(RelayOne.get_state())

rele_coil = RelayOne.stop()
# simulace fyzickeho rele
if rele_coil == 0:
    RelayOne.state = 0
print(RelayOne.get_state())

print(RelayOne.get_info())


RelayOne = RelaySSR("rele", rele_state)

print(RelayOne.get_state())

rele_coil = RelayOne.start()
print(RelayOne.get_state())

rele_coil = RelayOne.stop()
print(RelayOne.get_state())

print(RelayOne.get_info())
