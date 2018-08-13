
# coding: utf-8

# # Deming Regression
# -------------------------------
# 
# This function shows how to use TensorFlow to solve linear Deming regression.
# 
# $y = Ax + b$
# 
# We will use the iris data, specifically:
# 
# y = Sepal Length and x = Petal Width.
# 
# Demming regression is also called total least squares, in which we minimize the shortest distance from the predicted line and the actual (x,y) points.
# 
# If least squares linear regression minimizes the vertical distance to the line, Deming regression minimizes the total distance to the line.  This type of regression minimizes the error in the y values and the x values.  See the below figure for a comparison.
# 
# <img src="../images/05_demming_vs_linear_reg.png" width="512">
# 
# To implement this in TensorFlow, we start by loading the necessary libraries.

# In[1]:


#load watermark
get_ipython().magic(u'load_ext watermark')
get_ipython().magic(u"watermark -a 'Gopala KR' -u -d -v -p watermark,numpy,matplotlib,nltk,sklearn,tensorflow")


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets
from tensorflow.python.framework import ops
ops.reset_default_graph()


# Start a computational graph session:

# In[3]:


sess = tf.Session()

# Set a random seed
tf.set_random_seed(42)
np.random.seed(42)


# We load the iris data.

# In[4]:


# Load the data
# iris.data = [(Sepal Length, Sepal Width, Petal Length, Petal Width)]
iris = datasets.load_iris()
x_vals = np.array([x[3] for x in iris.data]) # Petal Width
y_vals = np.array([y[0] for y in iris.data]) # Sepal Length


# Next we declare the batch size, model placeholders, model variables, and model operations.

# In[5]:


# Declare batch size
batch_size = 125

# Initialize placeholders
x_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# Create variables for linear regression
A = tf.Variable(tf.random_normal(shape=[1,1]))
b = tf.Variable(tf.random_normal(shape=[1,1]))

# Declare model operations
model_output = tf.add(tf.matmul(x_data, A), b)


# For the demming loss, we want to compute:
# 
# $$ \frac{\left| A \cdot x + b - y \right|}{\sqrt{A^{2} + 1}} $$
# 
# Which will give us the shortest distance between a point (x,y) and the predicted line, $A \cdot x + b$.

# In[6]:


# Declare Demming loss function
demming_numerator = tf.abs(tf.subtract(tf.add(tf.matmul(x_data, A), b), y_target))
demming_denominator = tf.sqrt(tf.add(tf.square(A),1))
loss = tf.reduce_mean(tf.truediv(demming_numerator, demming_denominator))


# Next we declare the optimization function and initialize all model variables.

# In[7]:


# Declare optimizer
my_opt = tf.train.GradientDescentOptimizer(0.25)
train_step = my_opt.minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)


# Now we train our Demming regression for 250 iterations.

# In[8]:


# Training loop
loss_vec = []
for i in range(1500):
    rand_index = np.random.choice(len(x_vals), size=batch_size)
    rand_x = np.transpose([x_vals[rand_index]])
    rand_y = np.transpose([y_vals[rand_index]])
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(temp_loss)
    if (i+1)%100==0:
        print('Step #' + str(i+1) + ' A = ' + str(sess.run(A)) + ' b = ' + str(sess.run(b)))
        print('Loss = ' + str(temp_loss))


# Retrieve the optimal coefficients (slope and intercept).

# In[9]:


# Get the optimal coefficients
[slope] = sess.run(A)
[y_intercept] = sess.run(b)

# Get best fit line
best_fit = []
for i in x_vals:
  best_fit.append(slope*i+y_intercept)


# Here is matplotlib code to plot the best fit Demming regression line and the Demming Loss.

# In[10]:


# Plot the result
plt.plot(x_vals, y_vals, 'o', label='Data Points')
plt.plot(x_vals, best_fit, 'r-', label='Best fit line', linewidth=3)
plt.legend(loc='upper left')
plt.title('Sepal Length vs Pedal Width')
plt.xlabel('Pedal Width')
plt.ylabel('Sepal Length')
plt.show()

# Plot loss over time
plt.plot(loss_vec, 'k-')
plt.title('Demming Loss per Generation')
plt.xlabel('Iteration')
plt.ylabel('Demming Loss')
plt.show()

