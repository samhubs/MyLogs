# Monocular depth for real-world measurement

<p class="post-meta">January 24, 2025 · 7 min read · Computer Vision</p>

Estimating depth from a single image is exciting on its own, but it gets much more interesting when we treat it as part of a measurement system. The practical question is not just whether a model can predict a plausible depth map, but whether that depth can help us recover real dimensions from an ordinary photo.

This post sketches a simple pipeline for doing exactly that.

## Motivation

Suppose we want to measure the width of a table or the height of an object from one image. A monocular depth model can provide relative geometric structure, but relative depth alone is not enough. We still need a way to anchor the scene to physical units and compensate for the distortions introduced by viewpoint.

The recipe below uses a reference object plus a depth estimator to make that jump from image space to metric space.

## A simple workflow

### 1. Capture a reference object

Place a calibration object in the scene and photograph it as cleanly as possible. A flat plate with known dimensions works well because it gives us a stable geometric prior. In the original note, the example assumes an 8 inch by 8 inch plate.

The goal of this object is simple: it gives us something in the scene with known physical size, which we can later use to estimate a conversion factor from pixels and depth values into real units.

### 2. Predict a depth map

Run a monocular depth estimation model on the image. One possible choice is [Marigold](https://arxiv.org/pdf/2312.02145.pdf), though the broader idea does not depend on one specific model.

At this stage, the output is usually a dense depth map that captures relative structure across the image. The model may be excellent at ranking near versus far regions while still being imperfect in absolute scale, so we treat the prediction as useful geometry that still needs calibration.

### 3. Estimate the target tilt

If the reference plate is intended to be vertical and the camera is roughly level, then the difference between the predicted depth at the top and bottom of the plate tells us something about tilt.

Let the measured depth difference be:

$$
d = \| Z_{\text{bottom}} - Z_{\text{top}} \|
$$

and let the true physical height of the plate be \(h\). Then an estimate of the tilt angle is:

$$
\theta = \arctan \frac{d}{h}
$$

This angle gives us a rough sense of how much the object is leaning away from the ideal front-facing setup.

## Correcting perspective distortion

Even with a good depth map, perspective distortion can ruin direct measurements. A square plate viewed at an angle no longer looks square in the image, so we need a geometric correction before we trust pixel distances.

### Homography

A homography is a \(3 \times 3\) transformation matrix that maps one planar view to another. For flat objects, it is the natural tool for undoing perspective distortion.

### Point selection

Choose at least four corresponding points on the reference object:

- their observed coordinates in the image
- their ideal coordinates in a front-facing undistorted view

These points should define a stable planar shape, typically a rectangle or square.

### Solving for the transform

Once the correspondences are known, solve for the homography matrix \(H\). This gives a mapping from distorted image coordinates to corrected planar coordinates.

### Applying the transform

Apply \(H\) either to the image itself or to the selected points you care about. After rectification, the reference object should look much closer to its true proportions, which makes later measurement steps more meaningful.

## Recovering a scale factor

After perspective correction, compare the corrected size of the reference plate in pixels against its true dimensions.

That ratio gives a conversion factor between image measurements and physical measurements. This is the bridge between model output and real-world scale.

## Lifting pixels into 3D

Now suppose we want to measure the distance between two image points \((x_1, y_1)\) and \((x_2, y_2)\), with associated depth values \(Z_1\) and \(Z_2\).

Using the camera intrinsics, we can recover approximate 3D coordinates:

$$
X = \frac{(x - c_x) \times Z}{f}
$$

$$
Y = \frac{(y - c_y) \times Z}{f}
$$

This yields:

$$
(X_1, Y_1, Z_1), \qquad (X_2, Y_2, Z_2)
$$

One practical note matters here: the depth value \(Z\) should reflect any calibration correction you applied earlier. If the raw monocular prediction is only relative, you need to rescale it before treating it as physical depth.

## Final measurement

Once both points are represented in 3D, the measurement becomes a standard Euclidean distance:

$$
\text{Distance} = \sqrt{(X_2 - X_1)^2 + (Y_2 - Y_1)^2 + (Z_2 - Z_1)^2}
$$

At that point, the original question has been transformed from "how large does this look in the photo?" into "how far apart are these recovered 3D points?"

## Closing thought

What I like about this setup is that it combines learned perception with classical geometry instead of asking one model to do everything. The depth model gives structure, the reference object gives scale, and projective geometry keeps the whole pipeline honest.

It is not magic, and it is not perfectly calibrated metrology. But for many practical settings, it is a very reasonable path from a single image to an approximate metric measurement.
