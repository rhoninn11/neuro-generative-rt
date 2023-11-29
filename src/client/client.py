
import time
import socket

from utils.pipe_queue import pipe_queue
from client_base import client_base
class client(client_base):
    def __init__(self, name="noname"):
        client_base.__init__(self, name)
        self.connect_ack = False
        self.disconnect_ack = False

    def progress_balance(self, progress):
        if progress == 0:
            time.sleep(0.01)

    def process_information(self, information_obj, out_pipe: pipe_queue):
        is_disconnect = "disconnect" in information_obj    
        if is_disconnect and not self.disconnect_ack:
            self.print(f"+++ diconnect obj recived")
            self.disconnect_ack = True

        is_connect = "connect" in information_obj    
        if is_connect and not self.connect_ack:
            self.print(f"+++ connect obj recived")
            self.connect_ack = True

        operate_normal = not is_connect and not is_disconnect   
        if operate_normal:
            
            out_pipe.queue_item(information_obj)
            

    def send_simple_obj(self, connection, key):
        simple_obj = { key:1 }
        try:
            self.send(connection, simple_obj, id=1)
            # self.print(f"+++ {key} obj sended")
        except:
            # self.print(f"!!! {key} obj send failed")
            pass
    
    def _pre_loop(self, connection: socket):
        self.connect_ack = False
        self.disconnect_ack = False
        self.disconnect_flag = False
        self.send_simple_obj(connection, "connect")

    def _post_loop(self, connection: socket):
        if self.connect_ack and not self.disconnect_ack:
            self.send_simple_obj(connection, "disconnect")
            self.disconnect_ack = True

    def _loop_body(self, connection: socket, out_queue: pipe_queue):
        not_disconnected_yet = not self.disconnect_ack and not self.disconnect_flag
        while not_disconnected_yet:
            recived_obj = self.recive_nb(connection)
            if recived_obj:
                self.process_information(recived_obj, out_queue)

    def connection_loop(self, connection: socket, out_queue: pipe_queue):
        self._pre_loop(connection)
        self._loop_body(connection, out_queue)
        self._post_loop(connection)
        


