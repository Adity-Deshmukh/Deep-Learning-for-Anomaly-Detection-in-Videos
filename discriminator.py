import numpy as np
import tensorflow as tf
import keras
from keras import layers,Sequential
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv3D, LeakyReLU, Conv3DTranspose
from keras.layers import AveragePooling2D, MaxPool3D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
from keras.models import Model

def create_discriminator_model():

    X_input = Input((16,128,128,3))

    #not sure about the axis in batch norm
    #do we also add dropout after batchnorm/pooling?

    #Convolutional Layers
    #changed the no of filters 
    X=Conv3D(filters=32,kernel_size=(2,2,2),padding="same")(X_input)
    X=BatchNormalization(axis=1)(X)
    X=Activation('relu')(X)
    X=MaxPool3D(pool_size=(2,2,2),strides=(2,2,2))(X)

    X=Conv3D(filters=64,kernel_size=(2,2,2),padding="same")(X)
    X=BatchNormalization(axis=1)(X)
    X=Activation('relu')(X)
    X=MaxPool3D(pool_size=(2,2,2),strides=(2,2,2))(X)
        
    X=Conv3D(filters=128,kernel_size=(2,2,2),padding="same")(X)
    X=BatchNormalization(axis=1)(X)
    X=Activation('relu')(X)
    X=MaxPool3D(pool_size=(2,2,2),strides=(2,2,2))(X)

    X=Conv3D(filters=128,kernel_size=(2,2,2),padding="same")(X)
    X=BatchNormalization(axis=1)(X)
    X=Activation('relu')(X)
    X=MaxPool3D(pool_size=(2,2,2),strides=(2,2,2))(X)

    #to add the 5th layer change the cap to 32 frames

    # X=Conv3D(filters=256,kernel_size=(2,2,2),padding="same")(X)
    # X=BatchNormalization(axis=1)(X)
    # X=Activation('relu')(X)
    # X=MaxPool3D(pool_size=(2,2,2),strides=(2,2,2))(X)


    #Fully connected layers

    X=Flatten()(X)

    X=Dense(256,activation='relu')(X)
    X=BatchNormalization()(X)
    #add batch norm to dense layer
    X=Dense(2,activation='softmax')(X)

    model=Model(inputs=X_input,outputs=X,name="Dicriminator")

    return model 

if __name__=="__main__":
    discriminator=create_discriminator_model()
    opt = keras.optimizers.Adam(lr=0.001)
    discriminator.compile(loss='binary_crossentropy',optimizer=opt,metrics=['accuracy'])
    print(discriminator.summary())





