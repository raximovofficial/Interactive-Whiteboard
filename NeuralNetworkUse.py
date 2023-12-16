import numpy as np
import scipy.special as sci

class neuralNetwork:
    def __init__(self, filename) -> None:
        file = np.load(filename)
        
        
        self.inodes = int(file['inn'])
        self.onodes = int(file['outn'])
        self.hnodes = int(file['hidn'])
        

        self.wih = file['wih']
        self.who = file['who']

        self.activation_function = lambda x: sci.expit(x)

    

    def query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T

        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

def UseThisShit(all_val):
    n = neuralNetwork("file.npz")
    an = np.argmax(n.query((np.asfarray(all_val[0:]) / 255 * .99) + .01))
    return an