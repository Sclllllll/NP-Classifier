import tensorflow as tf
import sys

print(tf.__version__)

# The export path contains the name and the version of the model
model = tf.keras.models.load_model(sys.argv[1])
export_folder = sys.argv[2]
model.save(export_folder)
