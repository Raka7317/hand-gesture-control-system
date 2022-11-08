# hand-gesture-control-system


                                                           GESTURE CONTROL SYSTEM
                        By (Rakesh kumar)

what is this project about?
In this project, I had  created a Hand Gesture based Presentation system. We will be able to move the slides back and forth along with a pointer and drawing capabilities. And to make it more usable we will add an erasing gesture as well.


Prerequisites:
>knowledge of ml and ai
>a  language like python
> all about opencv package
> mediapipe another module package
>knowledge of versions of python and modules that are goint to be used.


what is machine learning?
Machine learning (ML) is a discipline of artificial intelligence (AI) that provides machines with the ability to automatically learn from data and past experiences while identifying patterns to make predictions with minimal human intervention.

how this model work?
An ML Pipeline for Hand Tracking and Gesture Recognition
Our hand tracking solution utilizes an ML pipeline consisting of several models working together:
A palm detector model (called BlazePalm) that operates on the full image and returns an oriented hand bounding box.
A hand landmark model that operates on the cropped image region defined by the palm detector and returns high fidelity 3D hand keypoints.
A gesture recognizer that classifies the previously computed keypoint configuration into a discrete set of gestures.

MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs machine learning (ML) to infer 20 3D landmarks of a hand from just a single frame. 
 
