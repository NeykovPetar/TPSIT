class Packet:
   
    def __init__(self, data):
        
        self.data = data

    def to_bytes(self): 
    
        buffer = self.data

        return buffer
    
    @staticmethod 
    def from_bytes(buffer):

        data = buffer[0:]

        return Packet(data)