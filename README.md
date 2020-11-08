# Hackathon: Agritech project 

For this hackathon project, we used Custom Vision to create an image classification model. The model is used to classify images into either normal or containing bacteria or fungi in grape, grape leaves, and grape trees:

* Anthracnose Elsinoe ampelina
* black measles
* black rot Guignardia bidwelli
* Crown Gall Agrobacterium vitis
* Downy mildew Plasmopara viticola
* Grey Mold Botrytis cinerea
* Leaf blight Isariopsis Leaf Spot
* normal
* Powdery Mildew Erysiphe necator


We exported the model into a TFLite model to use as a part of an android app as well as a raspberry pi.

The android app example is forked from TensorFlow Examples (details below).

The TFLite model is imported into the app to create a really basic, user-friendly app where users can take an image, and the image is classified into the categories mentioned above. 

Similarly, the model is imported into raspberry pi (connected to a camera), where a really simple program where images can be classified into the categories above. 

The app is a great way for farmers to take images and monitor their harvests' health, while a raspberry pi can be used to continuously monitor the health of grapes trees against pests. 

Presentation and demo:


# TensorFlow Examples

<div align="center">
  <img src="https://www.tensorflow.org/images/tf_logo_social.png" /><br /><br />
</div>

<h2>Most important links!</h2>

* [Community examples](./community)
* [Course materials](./courses/udacity_deep_learning) for the [Deep Learning](https://www.udacity.com/course/deep-learning--ud730) class on Udacity

If you are looking to learn TensorFlow, don't miss the
[core TensorFlow documentation](http://github.com/tensorflow/docs)
which is largely runnable code.
Those notebooks can be opened in Colab from
[tensorflow.org](https://tensorflow.org).

<h2>What is this repo?</h2>

This is the TensorFlow example repo.  It has several classes of material:

* Showcase examples and documentation for our fantastic [TensorFlow Community](https://tensorflow.org/community)
* Provide examples mentioned on TensorFlow.org
* Publish material supporting official TensorFlow courses
* Publish supporting material for the [TensorFlow Blog](https://blog.tensorflow.org) and [TensorFlow YouTube Channel](https://youtube.com/tensorflow)

We welcome community contributions, see [CONTRIBUTING.md](CONTRIBUTING.md) and, for style help,
[Writing TensorFlow documentation](https://www.tensorflow.org/community/documentation)
guide.

To file an issue, use the tracker in the
[tensorflow/tensorflow](https://github.com/tensorflow/tensorflow/issues/new?template=20-documentation-issue.md) repo.

## License

[Apache License 2.0](LICENSE)
