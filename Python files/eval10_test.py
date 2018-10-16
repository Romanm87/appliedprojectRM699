#! /usr/bin/env python

# use this to test with test set after training

import csv
import os
os.chdir('c:\\Users\Roman\CNN-for-Twitter-Sentiment-Analysis-master')
os.getcwd()

import numpy as np
import tensorflow as tf
from tensorflow.contrib import learn
import sys
import data_helpers

# import own data
with open('cln_test44.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)
  
data_2 = []
for i in range(len(data)):
    b = ", ".join( repr(e) for e in data[i])
    c = b.split(",")
    data_2.append(c[1][2:len(c[1])-1])

# Parameters
# ==================================================

# Data Parameters
#tf.flags.DEFINE_string("positive_data_file", "polarity.pos",
 #                      "Data source for the positive data.")
#tf.flags.DEFINE_string("neutral_data_file", "polarity.neu",
 #                      "Data source for the neutral data.")
#tf.flags.DEFINE_string("negative_data_file", "polarity.neg",
 #                      "Data source for the positive data.")
tf.flags.DEFINE_string("positive_data_file", "polarity3_test.pos",
                       "Data source for the positive data.")
tf.flags.DEFINE_string("neutral_data_file", "polarity3_test.neu",
                       "Data source for the neutral data.")
tf.flags.DEFINE_string("negative_data_file", "polarity3_test.neg",
                       "Data source for the positive data.")
# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 32, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "./runs/1527533326/checkpoints", "Checkpoint directory from training run")
tf.flags.DEFINE_boolean("eval_train", False, "Evaluate on all training data")


# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

FLAGS = tf.flags.FLAGS
#FLAGS._parse_flags()
FLAGS(sys.argv)

print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")

# CHANGE THIS: Load data. Load your own data here
#if FLAGS.eval_train:
    
x_raw, y_test = data_helpers.load_data_and_labels(FLAGS.positive_data_file,
                                                     FLAGS.positive_data_file,
                                                     FLAGS.negative_data_file)
y_test = np.argmax(y_test, axis=1)
#else:
    #x_raw = ["a masterpiece four years in the making", "everything is off."]
 #   x_raw, y_test = data_helpers.load_data_and_labels(FLAGS.positive_data_file,
     #                                                FLAGS.positive_data_file,
      #                                               FLAGS.negative_data_file)
   # y_test = [1, 0]
#x_raw = data_2
#x_raw = ["hello this is neutral", "one two three four", "terrible bad catastrophe negative", "very good postive.", "how is it going today", "do not like bad", "very happy good fantanstic"]

# Map data into vocabulary
vocab_path = os.path.join(FLAGS.checkpoint_dir, '../vocab')
vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
x_test = np.array(list(vocab_processor.transform(x_raw)))

print("\nEvaluating...\n")

# Evaluation
# ==================================================
checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
graph = tf.Graph()
with graph.as_default():
    session_conf = tf.ConfigProto(
        allow_soft_placement=FLAGS.allow_soft_placement,
        log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        # Load the saved meta graph and restore variables
        saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
        saver.restore(sess, checkpoint_file)

        # Get the placeholders from the graph by name
        input_x = graph.get_operation_by_name("input_x").outputs[0]
        # input_y = graph.get_operation_by_name("input_y").outputs[0]
        dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

        # Tensors we want to evaluate
        predictions = graph.get_operation_by_name("output/predictions").outputs[0]

        # Generate batches for one epoch
        batches = data_helpers.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

        # Collect the predictions here
        all_predictions = []

        for x_test_batch in batches:
            batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
            all_predictions = np.concatenate([all_predictions, batch_predictions])

# Print accuracy if y_test is defined
if y_test is not None:
    correct_predictions = float(sum(all_predictions == y_test))
    print("Total number of test examples: {}".format(len(y_test)))
    print("Accuracy: {:g}".format(correct_predictions / float(len(y_test))))

# Save the evaluation to a csv
predictions_human_readable = np.column_stack((np.array(x_raw), all_predictions))
out_path = os.path.join(FLAGS.checkpoint_dir, "..", "prediction_test8.csv")
print("Saving evaluation to {0}".format(out_path))
with open(out_path, 'w') as f:
    csv.writer(f).writerows(predictions_human_readable)
    
    
    
    
    

##Results: (1527533326) batch size: 64, #epochs: 200, devset: 10%
#Total number of test examples: 10382
#Accuracy: 0.710557

##Results: (1528642167) batch size: 32, #epochs: 20, devset: 5%
#Total number of test examples: 10382
#Accuracy: 0.720381

##Results: (1528643923) batch size: 32, #epochs: 10, devset: 5%
#Total number of test examples: 10382 (3,244 iterations)
#Accuracy: 0.719129
 
##Results: (1528644533) batch size: 32, #epochs: 10, devset: 5%, lambda = 0.1
#Total number of test examples: 10382 (3,244 iterations)
#Accuracy: 0.717107

##Results: (1528645154) batch size: 32, #epochs: 10, devset: 5%, lambda = 0.5
#Total number of test examples: 10382 (3,244 iterations)
#Accuracy: 0.711424    