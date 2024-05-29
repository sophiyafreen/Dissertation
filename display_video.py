import cv2   
   
input = cv2.VideoCapture( 0 )   
   
while True:
    ret, frame = input.read()   
    if ret:
        cv2.imshow( "video output", frame )   
    if cv2.waitKey(1) & 0xFF == ord( 'x' ):
      break
   
input.release()   
cv2.destroyAllWindows()  