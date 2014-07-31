import numpy as np
import cv2
import csv
import sys, os
from PIL import Image

im=imread("IMAG19.jpg",1);
Mat thr,gray;
blur(src,src,Size(3,3));
cvtColor(src,gray,CV_BGR2GRAY);
Canny(gray,thr,50, 190, 3, false );
vector<vector<Point> > contours;
vector<Vec4i> hierarchy;
findContours( thr.clone(),contours,hierarchy,CV_RETR_EXTERNAL,CV_CHAIN_APPROX_SIMPLE,Point(0,0));

vector<vector<Point> > contours_poly(contours.size());
vector<Rect> boundRect( contours.size() );
vector<Point2f>center( contours.size() );
vector<float>radius( contours.size() );
vector<vector<Point> >hull( contours.size() );
for( int i = 0; i < contours.size(); i++ )
{
approxPolyDP( Mat(contours[i]), contours_poly[i], 10, true );
boundRect[i] = boundingRect( Mat(contours_poly[i]) );
minEnclosingCircle( (Mat)contours_poly[i], center[i], radius[i] );
convexHull( Mat(contours[i]), hull[i], false );

if( contours_poly[i].size()>15) // Check for corner
   drawContours( src, contours_poly, i, Scalar(0,255,0), 2, 8, vector<Vec4i>(), 0, Point() ); // True object
else
   drawContours( src, contours_poly, i, Scalar(0,0,255), 2, 8, vector<Vec4i>(), 0, Point() ); // false object
  //drawContours( src, hull, i, Scalar(0,0,255), 2, 8, vector<Vec4i>(), 0, Point() );
  // rectangle( src, boundRect[i].tl(), boundRect[i].br(), Scalar(0,255,0), 2, 8, 0 );
   //circle( src, center[i], (int)radius[i], Scalar(0,0,255), 2, 8, 0 );
}
imshow("src",src);
imshow("Canny",thr);
waitKey();
