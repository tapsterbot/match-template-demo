import os
import cv2

template = cv2.imread(os.path.join(os.getcwd(),'redbird.png'))
frame = cv2.imread(os.path.join(os.getcwd(),'frame.bmp'))

threshold = 5510000.0

res = cv2.matchTemplate(frame, template, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

w, h, _ = template.shape[::]
(x,y) = min_loc
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)


new_res = cv2.rectangle(frame, top_left, bottom_right, 255, 2)

cv2.imwrite('res.png',frame)

while(True):
  cv2.imshow('Match Template Demo',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# When everything done, release the capture
cv2.destroyAllWindows()

# if min_val < threshold:
# #if 1:
#     print ("%s < %s :-)" % (min_val, threshold))
#     new_res = cv2.rectangle(frame, top_left, bottom_right, 255, 2)
# else:
#     print ("%s > %s" % (min_val, threshold))