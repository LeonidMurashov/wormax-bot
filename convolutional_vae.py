import tensorflow as tf
import numpy as np

class CVAE(tf.keras.Model):
    def __init__(self):
        super(CVAE, self).__init__()
        self.latent_dim = 50
        self.inference_net = tf.keras.Sequential(
            [
                    tf.keras.layers.InputLayer(input_shape=(128, 128, 3)),
                    tf.keras.layers.Conv2D(
                            filters=32, kernel_size=3, strides=(2, 2), activation='relu'),
                    tf.keras.layers.Conv2D(
                            filters=64, kernel_size=3, strides=(2, 2), activation='relu'),
                    tf.keras.layers.Conv2D(
                            filters=128, kernel_size=3, strides=(2, 2), activation='relu'),
                    tf.keras.layers.Conv2D(
                            filters=256, kernel_size=3, strides=(2, 2), activation='relu'),
                    tf.keras.layers.Flatten(),
                    # No activation
                    tf.keras.layers.Dense(self.latent_dim * 2),
            ]
        )

        self.generative_net = tf.keras.Sequential(
                [
                    tf.keras.layers.InputLayer(input_shape=(self.latent_dim,)),
                    tf.keras.layers.Dense(units=8*8*256, activation=tf.nn.relu),
                    tf.keras.layers.Reshape(target_shape=(8, 8, 256)),
                    tf.keras.layers.Conv2DTranspose(
                            filters=128,
                            kernel_size=3,
                            strides=(2, 2),
                            padding="SAME",
                            activation='relu'),
                    tf.keras.layers.Conv2DTranspose(
                            filters=64,
                            kernel_size=3,
                            strides=(2, 2),
                            padding="SAME",
                            activation='relu'),
                    tf.keras.layers.Conv2DTranspose(
                            filters=64,
                            kernel_size=3,
                            strides=(2, 2),
                            padding="SAME",
                            activation='relu'),
                    tf.keras.layers.Conv2DTranspose(
                            filters=32,
                            kernel_size=3,
                            strides=(2, 2),
                            padding="SAME",
                            activation='relu'),
                    # No activation
                    tf.keras.layers.Conv2DTranspose(
                            filters=3, kernel_size=3, strides=(1, 1), padding="SAME"),
                ]
        )

    @tf.function
    def sample(self, eps=None):
        if eps is None:
            eps = tf.random.normal(shape=(100, self.latent_dim))
        return self.decode(eps, apply_sigmoid=True)

    def encode(self, x):
        mean, logvar = tf.split(self.inference_net(x), num_or_size_splits=2, axis=1)
        return mean, logvar

    def reparameterize(self, mean, logvar):
        eps = tf.random.normal(shape=mean.shape)
        return eps * tf.exp(logvar * .5) + mean

    def decode(self, z, apply_sigmoid=False):
        logits = self.generative_net(z)
        if apply_sigmoid:
            probs = tf.sigmoid(logits)
            return probs

        return logits
    
    def call(self, inputs):
        return self.decode(self.encode(inputs)[0], apply_sigmoid=True)