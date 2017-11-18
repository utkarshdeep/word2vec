import tensorflow as tf
from converter import convert_data
from onehotvector import x_train, y_train
def train_model():
    words, word2int, vocab_size = convert_data()
    x = tf.placeholder(tf.float32, shape=(None, vocab_size))
    y_label = tf.placeholder(tf.float32, shape=(None, vocab_size))

    EMBEDDING_DIM = 5 # you can choose your own number

    W1 = tf.Variable(tf.random_normal([vocab_size, EMBEDDING_DIM]))

    b1 = tf.Variable(tf.random_normal([EMBEDDING_DIM])) #bias

    hidden_representation = tf.add(tf.matmul(x,W1), b1)

    W2 = tf.Variable(tf.random_normal([EMBEDDING_DIM, vocab_size]))

    b2 = tf.Variable(tf.random_normal([vocab_size]))

    prediction = tf.nn.softmax(tf.add( tf.matmul(hidden_representation, W2), b2))

    sess = tf.Session()

    init = tf.global_variables_initializer()

    sess.run(init) #make sure you do this!

    # define the loss function:
    cross_entropy_loss = tf.reduce_mean(-tf.reduce_sum(y_label * tf.log(prediction), reduction_indices=[1]))

    # define the training step:
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy_loss)

    n_iters = 10000

    # train for n_iter iterations

    for _ in range(n_iters):
        sess.run(train_step, feed_dict={x: x_train, y_label: y_train})

        print('loss is : ', sess.run(cross_entropy_loss, feed_dict={x: x_train, y_label: y_train}))

    print(sess.run(W1))
    print('----------')
    print(sess.run(b1))
    print('----------')

if __name__ == '__main__':
    train_model()