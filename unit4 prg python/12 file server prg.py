import socket
port = 60000
s=socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(5)
print('Server listening...')
while True:
    conn, addr = s.accept()
    print('Got connection from',addr)
    data = conn.recv(1024)
    print('Server received',repr(data))
    filename = 'mytext.txt'
    f=open(filename,'rb')
    i=f.read(1024)
    while(i):
        conn.send(i)
        print('Sent',repr(i))
        i=f.read(1024)
        f.close()
        print('Done sending')
        conn.send('Thank you for connecting')
        conn.close()
