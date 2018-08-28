import tensorflow as tf
image_filename = "./images/chapter-05-object-recognition-and-classification/working-with-images/test-input-image.jpg"
filename_queue = tf.train.string_input_producer(
    tf.train.match_filenames_once(image_filename))

image_reader = tf.WholeFileReader()
_, image_file = image_reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file, channels=3)
sess = tf.Session()
init_op = tf.group(tf.global_variables_initializer(),tf.initialize_local_variables())
sess.run(init_op)
# coord = tf.train.Coordinator()
# threads = tf.train.start_queue_runners(coord=coord, sess=sess)
print(sess.run(image))