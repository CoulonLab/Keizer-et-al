// Crop (if there is a selection)
title=getTitle();
if (endsWith(title,".tif")) title1=substring(title,0,lengthOf(title)-4);
else title1=title;
getDimensions(w,h,c,s,f);

// Offset using background
makeRectangle(921, 230, 103, 373);
run("Scale...", "x=- y=- z=1.0 width=1 height=1 interpolation=Bilinear average process create title=tmp1");
run("Scale...", "x=- y=- z=1.0 width="+w+" height="+h+" interpolation=Bilinear average process create title=tmp2");
close("tmp1"); v0=getPixel(1,1);
imageCalculator("Subtract create 32-bit stack", title,"tmp2");
title2=title1+"_off0"; rename(title2);
close("tmp2");
//close(title);

// Normalize using whole image
selectWindow(title2);
makeRectangle(527, 415, 196, 232);
run("Scale...", "x=- y=- z=1.0 width=1 height=1 interpolation=Bilinear average process create title=tmp1");
run("Scale...", "x=- y=- z=1.0 width="+w+" height="+h+" interpolation=Bilinear average process create title=tmp2");
close("tmp1"); v0=getPixel(1,1);
imageCalculator("Divide create 32-bit stack", title2,"tmp2");
title3=title2+"_nrmd"; rename(title3);
run("Multiply...", "value="+v0+" stack");
resetMinAndMax();
close("tmp2");
//close(title2);

