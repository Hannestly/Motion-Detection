# Motion Detection algorithm #
disclaimer: The following algorithm utilizes OpenCV library to achieve three things

1. To display the image, and draw shape
2. Convert each frame into matrix
3. color video to gray scale 

### How to start ###
- Clone the repository
- If you don't have openCV2, numpy, imutils already downloaded, 
    1. open command line, open the directory to the cloned folder
    2. type 'pip install -r requirement.txt'
- Open the motion.py in IDE of your choice
- enter the address of the video you want to track by editing line <b>6</b>

```python
vid = cv2.VideoCapture('address of your video')
```
- compile the motion.py 

### Demo ###
<a href="https://gyazo.com/5a719ff04dead4a8717946ed5e3a5d9e"><img src="https://i.gyazo.com/5a719ff04dead4a8717946ed5e3a5d9e.gif" alt="https://gyazo.com/5a719ff04dead4a8717946ed5e3a5d9e" width="782"/></a>