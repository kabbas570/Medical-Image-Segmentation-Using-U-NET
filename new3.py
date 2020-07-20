import pyrealsense2 as rs
import numpy as np
import cv2
import os


framek=[]
PATH='/home/user01/data_ssd/Abbas/Depth_Estimsation/new/'
def main():
    try:
        config = rs.config()
        rs.config.enable_device_from_file(config,"20200711_151505.bag",repeat_playback=False)
        pipeline = rs.pipeline()
        config.enable_stream(rs.stream.depth, 640, 360, rs.format.z16, 30)
        pipeline.start(config)
        i = 0
        while True:
            print("Saving frame:", i)
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            depth_image = np.asanyarray(depth_frame.get_data())
            #framek.append(depth_image)
            np.save(PATH,depth_image+str(i))
            #cv2.imwrite(PATH+ str(i)+ ".png", depth_image)
            i += 1
    finally:
        pass

d=main()



f=np.load('140.npy')