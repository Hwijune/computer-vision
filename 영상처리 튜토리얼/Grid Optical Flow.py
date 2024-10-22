import numpy as np
import cv2

def draw_flow(img,flow,step=16, black=False):
    global width, height

    h,w = img.shape[:2]
    y,x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx,fy = flow[y,x].T
    lines = np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = np.int32(lines + 0.5)
    vis = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    if black:
        vis = np.zeros((height,width,3),np.uint8)

    cv2.polylines(vis,lines,0,(0,255,0))

    for(x1,y1),(x2,y2) in lines:
        cv2.circle(vis,(x1,y1),1,(0,255,0),-1)
    return vis

def draw_hsv(flow):
    h,w = flow.shape[:2]
    fx,fy = flow[:,:,0], flow[:,:,1]
    ang = np.arctan2(fy,fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)
    hsv = np.zeros((h,w,3),np.uint8)
    hsv[...,0] = ang*(180/np.pi/2)
    hsv[...,1] = 255
    hsv[...,2] = np.minimum(v*4,255)
    bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    return bgr

def warp_flow(img,flow):
    h,w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:,np.newaxis]
    res = cv2.remap(img,flow,None,cv2.INTER_LINEAR)

    return res

def advanced_optflow():
    global width,height

    cap = cv2.VideoCapture(0)

    ret,prev = cap.read()
    prevgray = cv2.cvtColor(prev,cv2.COLOR_BGR2GRAY)
    show_hsv = False
    show_glitch = False
    cur_glitch = prev.copy()

    blackscreen = False
    while True:
        ret,frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prevgray,gray,0.0,0.5,3,15,3,5,1.1,0)
        prevgray = gray

        frame2 = draw_flow(gray,flow,black=blackscreen)
        cv2.imshow('Grid Optical Flow',frame2)

        if show_hsv:
            vis_hsv = draw_hsv(flow)
            cv2.imshow('flow Hsv',vis_hsv)

        if show_glitch:
            cur_glitch = warp_flow(cur_glitch,flow)
            cv2.imshow('glitch',cur_glitch)

        ch = cv2.waitKey(60) & 0xFF
        if ch == 27:
            break

        if ch==ord('1'):
            show_hsv = not show_hsv
            print('HSV flow visualization is',['off','on'][show_hsv])

        if ch==ord('2'):
            show_glitch = not show_glitch
            if show_glitch:
                cur_glitch = frame.copy()
            print('glitch is',['off','on'][show_glitch])

        if ch==ord('b'):
            blackscreen = not blackscreen

    cap.release()
    cv2.destroyAllWindows()

advanced_optflow()