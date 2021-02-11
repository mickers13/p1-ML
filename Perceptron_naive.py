"""
Dit is mijn naive aanpak van de perceptron neural network.
Deze aanpak heb ik gedaan met de uitleg van wat er op canvas staat,
maar na wat tips van Thijs heb ik een tweede "wat meer voorbereidende" versie gemaakt die makkelijker
toe tepassen zou zijn op de volgende opdrachten.
Wat er naief aan is is dat de weight en input "vastgezet" zijn.
Maar de input hoeft niet eens opgeslagen teworden, en de weight moet aanpasbaar zijn.
"""
#mathvariables

e = 2.718281828459

def sigmoid(number):
    """ Sigmoid function, output between -1 and 1"""
    #  simple sigmoid function in preperation for opdracht 3
    #  not yet used, but fun to have.
    return 1/(1+e**-number)

def stepper(number):
    """Stepper function, output 0 or 1"""
    #  simple stepping function
    if number >= 0:
        return 1
    else:
        return 0

class Perceptron():
    def __init__(self,bias = 0,activation = stepper):
        # define a perceptron and a basic bias ( standard value is a bias of 0 )
        # basic function is a stepper, but you can define a other activation function ( like sigmoid. )

        self.inputs = list()
        self.bias = bias
        self.activation = activation

    def __str__(self):
        """
        Print info about this perceptron
        """
        print("All inputs of perceptron: (input,weight) ---")
        for i in self.inputs:
            print(i)
        print("---")
        print("Bias: ",self.bias)
        print("function: ",self.activation.__doc__)


    def add_input(self,input,weight):
        self.inputs.append([input,weight])


    def get_output(self):
        input_total = 0
        if len(self.inputs) > 0 :
            for i in self.inputs:# calculate input
                input_val = i[0]
                weight = i[1]
                input_total += input_val*weight
            net_input = input_total+self.bias
            return self.activation(net_input) #  Add the bias on the total.
        else:
            print("no inputs, cant output.")

class Neural_layer:
    def __init__(self):
        #define variables
        self.perceptrons = list()

    def add_perceptron(self,perceptron):
        self.perceptrons.append(perceptron)

    def mass_input(self,inputs):
        #input given inputs to all perceptrons in a layer ( for easy assigning. )
        perceptrons = self.perceptrons
        if len(perceptrons) > 0:
            for i in inputs:
                input_val = i[0]
                weight = i[1]
                for j in perceptrons:
                    j.add_input(input_val,weight)

    def activate(self):
        if len(self.perceptrons)>0:
            outputs = list()
            for i in self.perceptrons:
                outputs.append(i.get_output())
            return outputs
        else:
            print("Layer has no perceptrons, outputting 0 as standard value. "
                  "( this is a bug if this was not intended! )")
            return 0

    def __str__(self):
        """data about layer"""
        print("amount of perceptrons in layer: ", len(self.perceptrons))

class Neural_network:
    def __init__(self):
        #define variables
        self.layers = list()

    def add_layer(self,layer):
        self.layers.append(layer)


    def feed_forward(self):
        layers = self.layers
        for layernumber in range(len(layers)):
            if len(layers) > 0:
                outputs = list()
                outputs.append(layers[layernumber].activate())
                if layernumber+1 == len(layers): #last layer
                    return outputs
                else:
                    print("feeding inputs to next layer: ",layernumber+1," max layers: ", len(layers) )
                    layers[layernumber+1].mass_input(outputs) #input outputs into next layer.

            else:
                print("Network has no layers, please add these before running.")
                exit(1)
    def __str__(self):
        """data about network ( for more specific info requist data of specific perceptron / layer."""
        print("amount of layers in network: ",len(self.percentrons))

#  maak perceptron aan en defineer inputs.
perceptron1 = Perceptron(0.25,stepper)
perceptron1.add_input(1,0.25)
perceptron1.add_input(-2,1)
perceptron1.__str__()
#  maak perceptron aan en defineer inputs.
perceptron2 = Perceptron(0.25,stepper)
perceptron2.add_input(0,0.25)
perceptron2.add_input(-1,1)

#  maak Neural layer aan, en voeg eerder genoemde perceptrons toe.
layer1 = Neural_layer()
layer1.add_perceptron(perceptron1)
layer1.add_perceptron(perceptron2)

#  maak perceptron aan en defineer inputs.
perceptron3 = Perceptron(0.34,stepper)
perceptron4 = Perceptron(0.1,stepper)
perceptron5 = Perceptron(0.40,stepper)

#  maak Neural layer aan, en voeg eerder genoemde perceptrons toe.
layer2 = Neural_layer()
layer2.add_perceptron(perceptron3)
layer2.add_perceptron(perceptron4)
layer2.add_perceptron(perceptron5)

#  Maak neural network aan, en voeg de layers toe.
network1 = Neural_network()
network1.add_layer(layer1)
network1.add_layer(layer2)

#  Run de neural network door de feed_forward aan te roepen, retourneert 3 outputs
#  ( even veel als perceptrons in de laatste layer )

print("---\nRunning network: \n")
print(network1.feed_forward())
