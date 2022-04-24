# CNN Classification

ResNet50 is applied to do image classification. The data set contains 10 types of different Pokemon images. The network will be trained to classify these pictures into 10 categories. 

## Dataset

10 Classes of Pokemons, with 2446 images in total

![MarineGEO circle logo](/image/sample.png "Sample of the Dataset")




## Training
### Data Augmentation
* Horizontal Flipping (with the probability of 0.5)

### Model
* Resnet50
* With initial layers frozen

### Training Process
* Max number of epochs: 10
* Batch size: 20

