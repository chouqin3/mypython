def write_records_file(dataset, record_location):
    """
    Fill a TFRecords file with the images found in `dataset` and include their category.

    Parameters
    ----------
    dataset : dict(list)
      Dictionary with each key being a label for the list of image filenames of its value.
    record_location : str
      Location to store the TFRecord output.
    """
    writer = None

    # Enumerating the dataset because the current index is used to breakup the files if they get over 100
    # images to avoid a slowdown in writing.
    current_index = 0
    for breed, images_filenames in dataset.items():
        for image_filename in images_filenames:
            if current_index % 100 == 0:
                if writer:
                    writer.close()

                record_filename = "{record_location}-{current_index}.tfrecords".format(
                    record_location=record_location,
                    current_index=current_index)

                writer = tf.python_io.TFRecordWriter(record_filename)
            current_index += 1

            image_file = tf.read_file(image_filename)

            # In ImageNet dogs, there are a few images which TensorFlow doesn't recognize as JPEGs. This
            # try/catch will ignore those images.
            try:
                image = tf.image.decode_jpeg(image_file)
            except:
                print(image_filename)
                continue

            # Converting to grayscale saves processing and memory but isn't required.
            grayscale_image = tf.image.rgb_to_grayscale(image)
            resized_image = tf.image.resize_images(grayscale_image, 250, 151)

            # tf.cast is used here because the resized images are floats but haven't been converted into
            # image floats where an RGB value is between [0,1).
            image_bytes = sess.run(tf.cast(resized_image, tf.uint8)).tobytes()

            # Instead of using the label as a string, it'd be more efficient to turn it into either an
            # integer index or a one-hot encoded rank one tensor.
            # https://en.wikipedia.org/wiki/One-hot
            image_label = breed.encode("utf-8")

            example = tf.train.Example(features=tf.train.Features(feature={
                'label': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_label])),
                'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_bytes]))
            }))

            writer.write(example.SerializeToString())
    writer.close()

write_records_file(testing_dataset, "./output/testing-images/testing-image")
write_records_file(training_dataset, "./output/training-images/training-image")


# filename_queue = tf.train.string_input_producer(
#     tf.train.match_filenames_once("./output/training-images/*.tfrecords"))
# reader = tf.TFRecordReader()
# _, serialized = reader.read(filename_queue)
#
# features = tf.parse_single_example(
#     serialized,
#     features={
#         'label': tf.FixedLenFeature([], tf.string),
#         'image': tf.FixedLenFeature([], tf.string),
#     })
#
# record_image = tf.decode_raw(features['image'], tf.uint8)
#
# # Changing the image into this shape helps train and visualize the output by converting it to
# # be organized like an image.
# image = tf.reshape(record_image, [250, 151, 1])
#
# label = tf.cast(features['label'], tf.string)
#
# min_after_dequeue = 10
# batch_size = 3
# capacity = min_after_dequeue + 3 * batch_size
# image_batch, label_batch = tf.train.shuffle_batch(
#     [image, label], batch_size=batch_size, capacity=capacity, min_after_dequeue=min_after_dequeue)