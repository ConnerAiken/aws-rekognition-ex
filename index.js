const cv = require('opencv');

cv.readImage('./demo_images/gameplay.jpg', function (err, img) {
  if (err) {
    throw err;
  }

  const width = im.width();
  const height = im.height();

  if (width < 1 || height < 1) {
    throw new Error('Image has no size');
  }

  // do some cool stuff with img
  img.convertHSVscale();
  
  // save img
  img.save('./demo_images/gameplay-hsv.jpg');
});