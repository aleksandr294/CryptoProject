import socket,threading

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '127.0.0.1'
port = 5005
s.bind((host,port))
s.listen(5)
client_sockets = []

def handle_client(conn):
    while True:
        try:
            data = conn.recv(512)
            for x in client_sockets:
                try:
                    print(data)
                    x.send(data)
                except Exception as e:
                    print ("Error:",e)
        except:
            pass
print ("Listening")

while True:
    conn, addr = s.accept()
    client_sockets.append(conn)
    print ("Connection from",addr[0], "on port", addr[1])
    threading.Thread(target=handle_client, args=(conn,)).start()

#while not quit:
    #try:
        #data, addr = sock.recvfrom(1024)
        
        #if addr not in clients:
            #clients.append(addr)
        
        
        #print('[' + addr[0]+']=['+ str(addr[1])+']=['+itsatime+']/', end='')
        #print(data.decode('utf-8'))

        #for client in clients:
            #if addr != client:
                #sock.sendto(data, client)
    #except KeyboardInterrupt:
        #print('\n [Server Stopped]')
        #quit = True
#sock.close()