# bitLontra

from blockchain import blockexplorer
import csv

filename = '/home/felipe/Downloads/pub_keys.csv'

def loadfile(filename): #fuction to load csv file
    addr = []
    with open (filename, 'rb') as list_file:
        csvfile = csv.reader(list_file)
        for row in csvfile:
            addr.append(row[0].strip())
    return addr

def balance(address):    # fuction to see balance for 1 address
    address_stats = blockexplorer.get_address(address)
    balance = float(address_stats.final_balance) * 10**(-8)
    return round (balance, 8)

def saldo(filename):    # fuction to see balance of N addresses
    addr = loadfile(filename)
    balance = 0.
    for address in addr:
        addr_stats = blockexplorer.get_address(address)
        balance += addr_stats.final_balance * 10**(-8)
        #print balance
    return round(balance, 8)

def enviado(filename): #function to see sent volume
    addr = loadfile(filename)
    tt_sent = 0.
    for address in addr:
        addr_stats = blockexplorer.get_address(address)
        tt_sent += addr_stats.total_sent * 10**(-8)
        #print balance
    return round(tt_sent, 8)

def total(filename):
    addr = loadfile(filename)
    i = 0
    bal_par = 0.
    print " "
    print "Lista de enderecos bitcoin:"
    print " "
    for address in addr:
        i += 1
        bal_addr = balance(address)
        bal_par += bal_addr
        print str(i)+ " - " + address + ' - ' + str(bal_addr)
    print " "
    print "Saldo total: " + str(bal_par)
    return
