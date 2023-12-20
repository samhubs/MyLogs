Monocular 3D measurements



 Monocular depth estimation is an important tool for letting users measure any object in a given photo. This is how it can be achieved:

1. Place a reference object in the scene and take an image of the object standing heads-on



2. Use a deep learning approach to get the depth map - using a technique such as Marigold (https://arxiv.org/pdf/2312.02145.pdf)



3. Determine the Tilt Angle of the calibration target:

Assuming the plate is vertical and the camera is level, the difference in depth between the top and bottom points corresponds to the physical height difference due to the tilt.

The actual height of the plate is known (8 inches in your case).

Using trigonometry, the tilt angle θ can be estimated. If d is the difference in depth between top and bottom $\|Z_{\text{bottom}} - Z_{\text{top}}\|$ and ℎ is the actual height of the plate, then: 

$$ \theta = \arctan\frac{b}{h} $$



4. Correcting Perspective Distortion

To correct perspective distortion, we need to transform the coordinates in the image to what they would be if viewed head-on. This involves several steps:

    a. Homography Matrix

A homography is a 3x3 transformation matrix that maps points from one plane to another. It's used in perspective correction.

    b. Points Selection

Select at least four corresponding points on the object in the image and what their coordinates would be without distortion. These points should not be co-linear and should form a rectangle or square for an object like a flat plate.

    c. Calculating the Homography Matrix

The homography matrix H can be calculated using these point correspondences. This involves solving a set of linear equations derived from the point correspondences.

    d. Applying the Transformation

Once H is obtained, it's applied to the image or the object in the image to correct the perspective distortion. This transformation maps the coordinates from the distorted image to their undistorted locations.



5. Calculate the Conversion Factor

With the corrected dimensions of the plate in pixels, compare these to the actual dimensions (8"x8") to calculate the conversion factor.

6. Coordinate Transformation

Suppose we want to measure the width of the table, and we've identified two points on the table's edges in the depth map at pixel coordinates 

$(x_1, y_1) \text{ and } (x_2, y_2)$

Let's say the depth values at these points are $Z_1$ and $Z_2$ meters. To convert these to 3D coordinates, we use the formula:

$$ X = \frac{(x - c_x) \times Z}{f} $$
$$ Y = \frac{(y - c_y) \times Z}{f} $$

So, for both points, we calculate $(X_1, Y_1, Z_1)$ and $(X_2, Y_2, Z_2)$.

> **Note:**
> Make sure Z above is $Z_{pixel} \times k$ where $k$ is the correction factor.

5. Measurement

We measure the distance between these two points in 3D space using the Euclidean distance formula:

$$\text{Distance} = \sqrt{(X_2 - X_1)^2 + (Y_2 - Y_1)^2 + (Z_2 - Z_1)^2}$$

This way one can potentially measure `metric` distances between points given a single image. 