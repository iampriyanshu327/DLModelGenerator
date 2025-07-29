# A code to generate DeepLearning codes (neural network) and then train the model to generate the bot..

'''
AI Model builder!

A user enters: Build a model that classifies Cats and Dogs image..

Bot returns: .h5/code-file with the trained DeepLearning model to use,
'''

layers = []
layerSize = 3

numOfLayers = int(input("Enter the number of layers: "))

for i in range(numOfLayers):
    
    layer = []
    print(f"\nEnter {layerSize} elements for Layer{i + 1}: ")
    
    for j in range(layerSize):
        element = int(input(f"\nEnter Element{j + 1}: "))
        layer.append(element)
        
    layers.append(layer)
    
print(f"\nMy 2D list for Neural Network is: ")
print(layers)