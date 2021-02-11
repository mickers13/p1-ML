# mathvariables
"""
Betere versie waar de feedforward ook echt de inputs aan kannemen, zonder dat je deze moet setten
Ook heeft deze de xor en half adder.  beoordeel deze file aub :)
"""
e = 2.718281828459


def sigmoid(number):
    """ Sigmoid function, output between -1 and 1"""
    #  simple sigmoid function in preparation for opdracht 3
    #  not yet used, but fun to have.
    return 1 / (1 + e ** -number)


def stepper(number):
    """Stepper function, output 0 or 1"""
    #  simple stepping function
    if number >= 0:
        return 1
    else:
        return 0


class Perceptron:
    def __init__(self, weights, bias=0.0, activation=stepper):
        # define a perceptron, weights and a basic bias ( standard value is a bias of 0 )
        # basic function is a stepper, but you can define a other activation function ( like sigmoid. )

        self.inputs = list()
        self.weights = weights
        self.bias = bias
        self.activation = activation

    def __str__(self):
        """
        Print info about this perceptron
        """
        print("All weights of perceptron: ---")
        for i in self.weights:
            print(i)
        print("---")
        print("Bias: ", self.bias)
        print("function: ", self.activation.__doc__)

    def get_output(self, inputs):
        net_sub_total = 0
        for integer in range(len(inputs)):
            net_sub_total += inputs[integer] * self.weights[integer]
        net_total = net_sub_total + self.bias # Add the bias on the total.
        return self.activation(net_total) #apply the activation function ( step for perceptron )


class Neural_layer:
    def __init__(self, perceptrons):
        # define variables
        self.perceptrons = perceptrons

    def activate(self, inputs):
        amount_perceptrons = len(self.perceptrons)

        output = list()
        for perceptron_val in range(amount_perceptrons):
            output.append(self.perceptrons[perceptron_val].get_output(inputs))

        return output

    def __str__(self):
        """data about layer"""
        print("amount of perceptrons in layer: ", len(self.perceptrons),"info about peceptrons:")
        for i in self.perceptrons:
            i.__str__()


class Neural_network:
    def __init__(self, layers):
        # define variables
        self.layers = layers

    def feed_forward(self, inputs):
        temp = inputs
        for layer in self.layers:
            temp = layer.activate(temp)
        output = temp
        return output

    def __str__(self):
        """data about network ( for more specific info requist data of specific perceptron / layer."""
        print("amount of layers in network: ", len(self.layers))


or_gate = Perceptron(weights=[0.5,0.5],
                         bias=-0.5,
                         activation=stepper)


nand_gate = Perceptron(weights=[-0.5,-0.5],
                         bias=0.5,
                         activation=stepper)


layer1 = Neural_layer(perceptrons=[or_gate,nand_gate])

and_gate = Perceptron(weights=[0.5, 0.5],
                         bias=-1,
                         activation=stepper)


layer2 = Neural_layer(perceptrons=[and_gate])

xor_gate = Neural_network(layers=[layer1, layer2])


def waarheidprinter(testnet,hoeveelinputs):
    # print gegeven met het netwerk en hoeveelheid inputs dat er getest worden de waardheden.
    for i in range(hoeveelinputs):
        binairy = bin(i)[2:].zfill(2)
        print("network with input: ",binairy, " en output:", testnet.feed_forward(inputs=[int(binairy[0]),int(binairy[1])]),"\n -----")
print("waarheids tabel xor_gate")
waarheidprinter(xor_gate,4)

layer1 = Neural_layer(perceptrons=[or_gate,nand_gate])

semi_not_gate = Perceptron(weights=[0, -0.5],
                         bias=0,
                         activation=stepper)

layer2 = Neural_layer(perceptrons=[semi_not_gate,and_gate])

half_adder = Neural_network(layers=[layer1, layer2])
print("half adder: ")
waarheidprinter(half_adder,4)