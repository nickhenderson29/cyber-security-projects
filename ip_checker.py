import ipaddress
ip = input('Enter an ip address: ')
try:
    ip_obj = ipaddress.ip_address(ip)
    print ('ip version:', ip_obj.version)
    print ('ip Address:', ip_obj) 
    if ip_obj . is_private:
        print ('ip type:private')
    elif ip_obj . is_global:
        print (' ip type:public')
    else: print ('ip type : special-use / non-global')   
    print ('valid ip address')
except ValueError:
    print ('invalid ip address')
