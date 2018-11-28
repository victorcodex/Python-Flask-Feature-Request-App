from cryptography.fernet import Fernet

# Oh no! The code is going over the edge! What are you going to do?

def main():
    key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
    f = Fernet(key)
    message = 'gAAAAABb9-4nWm2AmHFkYalypHLV_HZANczId8ne40htxmzqCcShoxdFU6x4dVgnX18GPwCmBA1Igh5ALMkV7zpuAonOYFyJXk1-JNhG41xelGJHMp_M97-l_l7F1t0FSUS6jmd362vvAoVREQ6t28GHiphcUlTQluK7cBaULO_UjS6gNHdN3AWDqhcrDpieN7nRjGDy8nBB'

    print(f.decrypt(message))


if "__name__" != "__main__":
    main()
