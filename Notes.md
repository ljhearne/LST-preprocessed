## Notes on the LST fmriprep outputs   
Written by Amy Stringer

Thing's I'm looking out for are structural masks that cut off parts of brain or include too much of the non-brain mattter i.e. skull and other bone around the brain. Also whether there is any obvious warping or distortion in any of the frames 

### General Structure of Notes (try to be consistent) 

* subject number 
    - Obvious distortion y/n 
        If yes, note which runs and or which frames/section contain the distortions
    - Brain mask notes - brain mask and tissue seg of T1  
        - which runs/frames contains extra 
        - which runs/frames are missing brain portions 

### Here goes 

#### subject that don't have blurry func/anat alignment results 

#### General comments 

* sub-02 
    - Distortion? 
        - scans seem kinda blurry so a little hard to tell 
    - Brain mask notes - brain mask and tissue seg of T1 
        - x = -1 seems to miss quite a lot of the cortex and the internal white matter outlines seems very skewed 
        - A few masks in the y direction seems to cut out a little V of cortex matter in the top centre of each scan  

* sub-04
    - Distortion? 
        - blurry func + anat alignment 


* sub-05 
    - Distortion? 
        - alignment of func to T1 really blurry across all runs (task and rest)
    - Brain mask - T1 
        - z = -22 - red outline contains larger chunk on non brain

* sub-06 
    - Distortion? 
        - func + anat allignment super blurry

* sub-08 
    - Distortion? 
        - task LST run 2: func/anat alignment looks like it results in a bit of warping - almost like like it's tried a twist/rotate to fit 
    - brain mask - T1 
        - some odd outlining at y = 53 
        - some small brain chunks cut out at y = -6 

* sub-09 
    - Distortion? 
    - Brain mask T1 
        - y = 63 little black unattached circles included in mask 
        
* sub-10 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is 3.1e-08 radians. The difference in translation is 7.1e-15mm."
    - Brain mask T1 
        - y = 72 has some little unattached circles forming part of the mask, can't really tell if they include brain matter or simply nothing 
        - z = -7 the red mask retains some non brain matter behind the eyes 

* sub-11
    - Distortion? This one seems even blurrier than the others in all the fmri runs 

* sub-13 
    - Distortion? 
        -Yes. the alignments of func and anat MRI data looks rotationally warped 
        - Parts of cerebellum appear to be missing from the functional scans. Visible in the y and x plane views as a perfectly flat line across the bottom 

* sub-14 
    - Brain mask T1 
        - y = 69 additional small circle of mask in bottom right of image 
        - z = -8 some addition blackness at the front of the brain counted as brain matter 

* sub-15 
    - Brain mask T1 
        - y = 1 looks as though the mask has cut of some outer brain matter near the brain stem 
    - Distortion? 
        - Flat line across bottom of images in the y plane, cutting off some of the cerebellum in func/anat alignment figures 

* sub-17 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -1.8e-07 radians. The difference in translation is 1e-14mm."

* sub-18 
    - Brain mask T1 
        - y = -14 black spot included as brain matter at top of brain

* sub-19 
    - Brain mask T1 
        - y = -1 mask cut off some brain matter around the brain stem
        - Distortion? 
            - Flat line across the bottom of the functional images, visible in the y and x plane views 

* sub-20
    - Brain mask T1 
        - z = -28 slice just looks quite weird, not sure if it's just because of the slice position though...
    - Distortion? 
        - Flat line across the bottom of the functional images, visible in the y and x plane views 


* sub-21 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is 0.0002 radians. The difference in translation is 7.1e-15mm."
    - Distortion? Blurrier than the rest 
    - Brain mask T1 
        - z = -15 some blackness included near in the mask near the eyes 

* sub-22 
    - Brain mask T1 
        - z = -22 black area included in mask behind the eyes 

* sub-23 
    - Brain mask T1 
        - z = -29 mask includes a section in the top middle section of the image that looks more like nose than brain 
        - z = -23 mask line a little too far reaching toward eyes 
    - Distortion? 
        - Images in bottom row seem to have a perfect straight line across the bottom - cutting off some of the cerebellum. Seems to be missing in the second row too, maybe the scanner position was just wrong? 

 * sub-24 
    - Distortion? 
        - I can see a similar thing to the previous subject in the anat/func alignment images. The functional scan seems to be missing some of the cerebellum along the bottom row, and in the side view this seems to be consistent. 
    - Brain mask T1 
        - this brain looks odd, like it's missing all the CSF regions altogether 


* sub-25 
    - Brain mask T1    
        - x = 7, the mask dips in at the top of the brain and it's hard to tell whether it should have or not i.e. whether or not. A similar thing can be seem at x = -11 which there is a dip in the mask that seems to cut out a portion of what could be cortex, or simply the other tissues surrounding the brain. 
        - This brain generally looks a little weird, though I can't pin point why. The CSF regions looks quite large and very dark, and appear to be in some locations that are inconsistent with the other scans in the population group 
    - Distortion? 
        - base of brain seems to be slightly cut off in the funnctional scans. Visible in the bottom row of the anat/func alignment figures 

* sub-26 
    - Brain mask T1 
        - y = 69 two small circular sections at base of brain included in mask despite the scan area showing up black 
        - z = -19 some blackness included in mask in the top middle right area of the scan 
    - Distortion? 
        - in the anat/func alignment figures the scans look quite vertically strecthed in order to fit, and they are quite a bit blurrier than other subjects 

* sub-27
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -3.1e-05 radians. The difference in translation is 7.1e-15mm."

* sub-28 
    - Distortion? 
        - Func/anat alignments figures seem quite blurry compared to others 

* sub-29 
    - Brain mask T1 
        - Some weird stuff going on at z = -31. Looks like it's given two red outlines toward the front of the head 
        - x = -22, some wonky mask line at the front of head 
    - Distortion? 
        - func/anat figures seem to have stretched the func image quite a lot, blurring the lines between regions significantly 

* sub-30 
    - Brain mask T1 
        - z=-28 mask seems to include nose area 
    - Distortion? 
        - in the y view, func scans are flat at the bottom, in some cases cutting off the cerebellum, or part of it  

* sub-31 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is 1.5e-05 radians. The difference in translation is 7.9e-15mm."
    - Brain mask T1 
        - z = -26, mask a little wonky at the front behind the eyes, looks like it may have cut out some brain matter around here 
        - y = 73 mask seems to include the eyes 
    - Distortion? 
        - functional scans have a flat line across the bottom in the y plane view 

* sub-32 
    - Brain mask T1 
        - z = -25 looks a little wonky behind the eyes. Either it's included parts it sould have or excluded a part it should have, a little hard to tell 
    - Distortion? 
        - I suspect the participant was positioned oddly for the functional scan as the cut off section at the base of the brain in the y plane is severe enough that it's also visible in the x plane images 
        - The z = -48 image also seems to have uneven signal (?) in the -z direction images 

* sub-33 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -1.5e-07 radians. The difference in translation is 3.6e-15mm."
    - Distortion? 
        - as in the previous subject, cut off area in the functional scan visible in both the y and x planes views 
        - quite blurry compared to others 

* sub-34 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -2.1e-08 radians. The difference in translation is 7.9e-15mm."
    - Brain mask T1 
        - y = 55 mask looks like it tried to include some eye 

* sub-37
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -1.8e-06 radians. The difference in translation is 0mm."
    - Brain mask T1 
        - z = -25 looks a little wonky behind the eyes. Either it's included parts it sould have or excluded a part it should have, a little hard to tell

* sub-38 
    - Brain mask T1 
        - mask includes some black in top of image in z = -18 and y = 61 
    - Distortion? 
        - Func/amnat alignment figure shows the functional image cut off some of the cerebellum in a few slices - visible in  y > -3 and x > -16

* sub-39 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -7e-06 radians. The difference in translation is 3.6e-15mm."
    - Brain mask T1 
        - z = -19 Some weird mask behaviour 
        - z = -12 Mask includes black non brain area         
        - y = 62 Mask attempts to include eyes  
    - Distortion? 
        - Func/anat alignment figure shows the functional scan slightly cuts out some of the brain stem 

* sub-40 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -1.9e-05 radians. The difference in translation is 0mm."
    - Brain mask T1 
        - z = -23 mask seems to include some non brain matter behind the eyes 
        - y = 64 mask tries to include the eyes 
    - Distortion? 
        - functional images look blurrier than others 

* sub-41 
    - Brain mask T1 
        - The brain outline in this scan isn't incredibly clear and so the mask looks like it get a little confused. E.g. y = -31 the right hemisphere looks smaller than the left and the mask seems to include some black space as if to counter this. Not sure if an issue with the scan or not. 
        - This also happens in y = 1, y = 17 and the x plane across all slices 
    - Distortion? 
        - Functional scans incredibly blurry

* sub-42 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -1.8e-08 radians. The difference in translation is 7.9e-15mm."

* sub-43 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is 2e-05 radians. The difference in translation is 7.1e-15mm."
    - Brain mask T1 
        - z = -32 mask contains some non brain matter in the nose area 

* sub-44 
    - Brain mask T1 
        - z = -29 and z=-23 both seems to contain nose in the mask 
    - Distortion? 
        - Functional scans don't look distorted, but they also don't look like much of anything ... 

* sub-45 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -2.9e-06 radians. The difference in translation is 1e-14mm."
    - Brain mask T1 
        - y = 68, can't tell if mask has included eyes or if this is brain matter due to the outlines covering the actual image 
        - x = 21, looks like the mask may have missed some brain matter toward the front of the brain 

* sub-46 
    - Distortion? 
        - functional scan appears to cut off some of the cerebellum and brain stem, visible in the anat/func alignment figure in both the x and y plane views 

* sub-47 
    - Brain mask T1 
        - y = 64 looks to have included the eyes in the mask 
        - z = -32 can't tell if brain matter of nose 
    - Distortion? 
        - The func/anat alignment figure seems to show that the functional image was vertically stretched or squashed to align the images and in some instances i.e. z = -25 this doesn't look right 

* sub-48 
    - Brain mask T1 
        - y = 64 mask looks like it includes the eyes 
        - y = 30 hard to tell but looks like the mask has ignored the cerebellum 
    - Distortion? 
        - Functional scans cup off at the base of brain - visible in both the x and y plane views of the func/anat alignment figure 

* sub-49 
    - Brain mask T1 
        - y = 62 mask includes eyes
    - Distortion? 
        - functional scans cut off at the base - visible in both y and x slices in the anat/func alignment figures 
* sub-51 
    - Brain mask T1 
        - y = 61 the mask includes the eyeballs 
        - z = -30 fairly sure the mask is including the nose here 
    - Distortion? 
        - Some of the boundary slice scans in the x plane of the func/anat alignment figure look stretched beyond recognition 

* sub-52 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is 0.00012 radians. The difference in translation is 0mm."
    - Brain mask T1 
        - Looks like z = -21 and z = -14 the actual image seems to be cut off at the front of the head though this doesn't seem to cut out any brain matter so i think the mask is okay. 
        - That said, the mask looks like it include nose tissue 
        - y = 63 also includes some eyeball in the mask 
        - y = 13 has some black area included in the mask 
    - Distortion? 
        - functional scans cut of at the base of the head, visible in both x and y plane views 

* sub-53 
    - Brain mask T1 
        - z = - 25 looks like it more obviously includes nose tissue/bone structure 
        - x = -6 looks a little rough around the edges of the mask 
    - the func/anat alignment images looks a little weird, can't tell why but they also quite blurry 

* sub-54 
    - Brain mask T1 
        - z = -27 in the centre nose area at the front of the head the mask includes some non brain tissue 
        - also visible in all z < 4 scans 
     - Distortion? 
        - Functional scans are cut off at the base of the head, visible in the x and y plane views 

* sub-55 
    - Brain mask T1 
        - z = -13 mask includes nose 
        - y = 65 mask includes eyes 
    - Distortion? 
        - func scans looks blurrier than the others 

* sub-56 
    - Brain mask T1 
        - z = -27 nose 
        - z = -19 a little nlack non brain tissue included in mask at front of head 
    - Distortion? 
        - base of head cut off in the functional scans visible in both the x and y plane views 

* sub-57 
    - Brain mask T1 
        - z = -26 includes nose 
        - y = 3 seems to miss some brain matter at top and bottom right of image 
    - Distortion? 
        - Functional images cut of at base of head visible in x and y plane views 

* sub-58 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -4.4e-07 radians. The difference in translation is 1e-14mm."
    - Distortion?
        - The functional scans in the func/anat alignment figures looks a little wonky 
        - Also cut off at the base of the head 

* sub-59 
    - The structural scan for this subject looks very off. Big dark holes in the CSF regions - much larger than the others and the mask seems so include more black around the edges than other subjects - worth checking 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is 2.8e-07 radians. The difference in translation is 7.1e-15mm."
    - Functional scans in the func/anat alignment figure look as if they're sliced off across the front of the brain this time, AND at the base. Not great scans 

* sub-60 
    - Brain mask T1 
        - z = -34, mask includes a big black chunk of non brain at the front section of the head 
    - Distortion? 
        - functional scans cut off at base 

* sub-61 
    - Anatomical scans look a little wonky and distorted 
    - Brain Mask T1 
        - z = -18 is that nose? 
    - Functional scans cut off at base of head 

* sub-62 
    - "Note on orientation: qform matrix overwritten: The qform has been copied from sform. The difference in angle is -1.8e-08 radians. The difference in translation is 7.1e-15mm."
    - Brain mask T1 
        - z = -32 nose area included in mask 
        - x = -10 mask seems to cut out some brain tissue around the right hand side edge 
        - y = 64 mask includes eyes 
    - Distortion? 
        - Cut of base of brain. More severe that many of the earlier scans, visible in x and y plane views 

* sub-63 
    - Brain mask T1 
        - z = -32 mask includes some questionable content in front middle area 
        - x = -9 mask seems to cut out some brain tissue around the lower front of brain edge 
    - Distortion? 
        - Another quite severe cut of area at base of head visible in both x and y plane directions 

* sub-64 
    - Brain mask T1 
        - z = -18 questionable inclusion... looks like nose but can't quite tell 
        - y = 66 Is that eyes? 

* sub-65 
    - Brain mask T1 
        - z = -20 nose in mask 
        - y = 72 can't tell if this includes eyes or not but the mask areas are disjoint 
        - y = 19 mask seems to cut off some of the cerebellum on the right side 
    - Distortion? 
        - functional scans cut of at base of head 
        






