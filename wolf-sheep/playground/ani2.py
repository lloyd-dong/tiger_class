import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import time
import random


class example():

    def __init__(self, nframes = 17, interval = 1000):

        self.image = np.zeros((1000,1000), dtype=np.float32)
        self.total_time = 0
        self.nframes = nframes
        self.interval = interval
        self.plotting()

    def plotting(self):

        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111)
        video_object = ax.imshow(self.image, vmin=0, vmax=1000, animated=True)
        #creating a timer object and setting an interval of 
        # nframes * interval + time to first draw milliseconds
        timer = fig.canvas.new_timer(interval = self.nframes*self.interval+300) 
        timer.add_callback(plt.close)

        def init():
            self.image[:, :] = np.random.rand(1000, 1000)
            video_object = ax.imshow(self.image)
            # start timer
            timer.start()
            return(video_object,)

        def updatefig(k):
            start_time = time.time()
            #self.image[:,:] = np.random.rand(1000,1000) # I leave this here as this is how it should be done
            for i in range(self.image.shape[0]): # slow looping 
                for j in range(self.image.shape[1]):
                    self.image[i,j] = random.uniform(0,1000)

            video_object.set_array(self.image)
            self.total_time += time.time() - start_time
            print('time in loop: ' + repr(time.time() - start_time)[0:5] + "- " +str(k))
            return(video_object,)

        ani = animation.FuncAnimation(fig = fig, func = updatefig, init_func = init,
                                      frames = self.nframes, repeat=False,
                                      interval=self.interval, blit=True )

        plt.show()

        print('Total time loop : ' + repr(self.total_time))

outer_time = time.time()
example(nframes = 17, interval = 1000)
print('Total time until close fig: ' + repr(time.time() - outer_time))