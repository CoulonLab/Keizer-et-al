spotDetectionCutoff=10;

title=getTitle();
getDimensions(w,h,c,s,f);

run("Stack to Hyperstack...", "order=xyczt(default) channels=1 slices=1 frames="+(s*f)+" display=Grayscale");
getDimensions(w,h,c,s,f);

run("Gaussian Blur...", "sigma=20 stack");
resetMinAndMax();

listImages=""
for (i=1; i<=f; i++) {
	selectWindow(title);
	Stack.setFrame(i);
	run("Find Maxima...", "prominence="+spotDetectionCutoff+" output=[Single Points]");
	name="tmp_"+IJ.pad(i,4);
	rename(name);
    listImages=listImages+"image"+i+"="+name+" ";         
}
run("Concatenate...", "open "+listImages+"image"+i+"=[-- None --]");
rename("maxima");
run("32-bit");
run("Gaussian Blur...", "sigma=1.70 stack");
resetMinAndMax(); run("16-bit"); setMinAndMax(0, 4000);

title2=substring(title,0,lengthOf(title)-4)+"_maxima.tif";
saveAs("Tiff", "/Users/acoulon/Dropbox (UMR3664)/CoulonLab/data/Antoine/20211208/analysis_bead_attraction/"+title2);

run("Merge Channels...", "c1="+title+" c2="+title2+" create");
Stack.setChannel(1); run("Green");
Stack.setChannel(2); run("Grays");

doCommand("Start Animation [\\]");


