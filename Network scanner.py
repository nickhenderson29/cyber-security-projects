import socket

target = input ('Enter IP Address:')
print (f'you entered: {target}')

start_port = int(input( 'Enter start port: '))
end_port = int(input(' Enter end_port '))

for port in range (start_port, end_port + 1):

    print (f'checking port {port}')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                     
                     
    result = sock.connect_ex((target, port))

    print (f'port {port} returned {result}')


    if result == 0:
       print (f'port {port} is open')
       
    else:
        
        print(f'port {port} is CLOSED')


sock.close()



