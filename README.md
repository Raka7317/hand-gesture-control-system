# Hand-Gesture Controlled Presentation Viewer with Advanced Features

This project is an enhanced version of a hand-gesture-controlled presentation viewer. It allows users to seamlessly navigate through slides, annotate (write or erase) on the slides, and overlay a webcam feed for interactivity. The program is implemented using Python, OpenCV, and the `cvzone.HandTrackingModule`.

---

## Features

1. **Hand Tracking**: Detects and tracks hand gestures using `cvzone.HandTrackingModule`.
2. **Slide Navigation**: Swipe left or right with gestures to move between slides.
3. **Annotation Tools**: Write or erase directly on the slides using gestures.
4. **Live Webcam Feed**: Displays a real-time webcam overlay on the slides.
5. **Customizable Resolution**: Adjusts the size of the webcam feed overlay.

---

## Prerequisites

Ensure the following libraries are installed:

- Python 3.x
- OpenCV (`cv2`)  
  ```bash
  pip install opencv-python
  ```
- `cvzone`  
  ```bash
  pip install cvzone
  ```
- `numpy`  
  ```bash
  pip install numpy
  ```

---

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hand-gesture-presentation.git
   cd hand-gesture-presentation
   ```

2. Prepare a folder named `presentation` in the same directory. Place your presentation slides (images) in this folder.

3. Run the program:
   ```bash
   python main.py
   ```

---

## Code Explanation

### Key Sections
1. **Hand Tracking Setup**  
   Using the `cvzone.HandTrackingModule`, the program detects hand gestures and tracks the position of hands.
   ```python
   from cvzone.HandTrackingModule import HandDetector
   detector = HandDetector(detectionCon=0.8, maxHands=1)
   ```

2. **Reading Presentation Slides**  
   The slides are loaded from the `presentation` folder, sorted in ascending order based on file name length.
   ```python
   folderPath = "presentation"
   pathImages = sorted(os.listdir(folderPath), key=len)
   ```

3. **Slide Navigation**  
   Swiping gestures are used to navigate through the slides:
   - **Swipe Left**: Move to the next slide.
   - **Swipe Right**: Return to the previous slide.

4. **Annotation Mode**  
   - **Write**: Use your finger to draw on the slide. 
   - **Erase**: Enable eraser mode to clear annotations.
   ```python
   if gesture == "write":
       # Draw on the slide
   elif gesture == "erase":
       # Erase annotations
   ```

5. **User Control**  
   Press **`q`** to quit the application.

---

## Example Directory Structure

```
hand-gesture-presentation/
│
├── main.py
├── presentation/
│   ├── slide1.jpg
│   ├── slide2.jpg
│   ├── slide3.jpg
```

---

## Controls

1. **Gesture-based Controls**:
   - **Swipe Left**: Next slide.
   - **Swipe Right**: Previous slide.
   - **Write**: Use gestures to annotate slides.
   - **Erase**: Switch to erase mode and clear annotations.

2. **Keyboard Controls**:
   - **`q`**: Quit the program.

---

## Future Enhancements

1. Add customizable pen colors and sizes for annotations.
2. Integrate OCR to extract text from slides for easier annotation.
3. Add support for controlling external presentation software like PowerPoint.
