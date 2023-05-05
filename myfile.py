
fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
vid=cv2.VideoCapture(0)
while True:
    flag, img=vid.read()
    if flag:
        faces=fd.detectMultiScale(img,1.1,5,minSize=(50,50)) # 1.1=scaleFactor & 5=minNeighbors we can define min size==minSize=(50,50)
        
        np.random.seed(50)
        colors=np.random.randint(0,255,(len(faces), 3)).tolist() #len(faces) for multiple colors
        i=0
        for x,y,w,h in faces:
             cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=colors[i])
             i+=1

        

        cv2.imshow('preview', img)
        key=cv2.waitKey(1)
        if key==ord('q'):   
             break
    else:
            break
    sleep(0.1)
cv2.destroyAllWindows()
vid.release() #use for shut off camera