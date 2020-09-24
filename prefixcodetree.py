class PrefixCodeTree:
    def __init__(self, data = 'Empty'):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, codeword, symbol):
        tmp = self
        #print(codeword)
        codeLen = len(codeword)
        i = 0
        while i < codeLen:
            if i == codeLen - 1:
                if codeword[i] == 1:
                    tmp.right = PrefixCodeTree(symbol)
                    #print(tmp.data)
                    tmp = self
                    #print(tmp.data)
                else:
                    tmp.left = PrefixCodeTree(symbol)
                    #print(tmp.data)
                    tmp = self
                    #print(tmp.data)
            else:
                if codeword[i] == 1:
                    if tmp.right is None:
                        tmp.right = PrefixCodeTree()
                    tmp = tmp.right
                else:
                    if tmp.left is None:
                        tmp.left = PrefixCodeTree()
                    tmp = tmp.left
            i += 1

    def decode(self, encodedData, datalen):
        
        #Transform encodedData to bit string
        binstr = ''.join(f'{x:08b}'for x in encodedData)
        #Remove whitespace from binstr
        binstr = ''.join(binstr.split())
        #print(binstr)
        binstr = binstr[:datalen]
        #print(binstr)

        message = ''
        tmp = self
        for i in binstr:
            #print(i)
            #print(type(i))
            if i == '1':
                tmp = tmp.right
                #print('go right ' + tmp.data)
            else:
                tmp = tmp.left
                #print('go left '+ tmp.data)
            if tmp.data != 'Empty':
                #print(tmp.data)
                message += tmp.data
                tmp = self
        return message

#Test:
'''
codeTree = PrefixCodeTree('root')
codebook = {
  'x1': [0],
  'x2': [1,0,0],
  'x3': [1,0,1],
  'x4': [1,1]
}
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)
message = codeTree.decode(b'\xd2\x9f\x20', 21)
m = 'x4x1x2x3x1x1x4x4x2x2'
print(m == message)
'''
