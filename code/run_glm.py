
from dataset import ImagingDataset
from nilearn.glm.first_level import FirstLevelModel
from nilearn.interfaces.bids import get_bids_files
from task_event_models import motor_model, motor_contrasts, reasoning_contrasts
import numpy as np
import nibabel as nib

# get dataset
subj_list = list(np.loadtxt('subject_list.txt', dtype='str'))
ds = ImagingDataset(subj_list, '../data/')

# basic parameters
event_model = 'reasoning'
task = 'LST'
smooth = 4.0
out_dir = '../data/derivatives/results/'

for subj in ds.raw_subject_list():
    print(subj)
    try:
        # create a GLM object with more or less default params
        # get image specs
        t_r, slice_time_ref = ds.get_tr_and_slice_time(subj=subj)

        # create GLM object with almost entirely default parameters
        model = FirstLevelModel(t_r=t_r,
                                slice_time_ref=slice_time_ref,
                                hrf_model='spm',
                                smoothing_fwhm=smooth,
                                standardize=True,
                                subject_label=subj,
                                verbose=1)

        # get preprocessed images
        img_files = get_bids_files(ds.deriv_path, modality_folder='func',
                                file_tag='bold', file_type='nii.gz',
                                filters=[('task', task),
                                            ('space', 'MNI152NLin2009cAsym')],
                                sub_label=subj)
        n_runs = len(img_files)

        # get task events
        event_files = get_bids_files(ds.bids_path, modality_folder='func',
                                    file_tag='events', file_type='tsv',
                                    sub_label=subj)
        assert len(
            event_files) == n_runs, 'Number of images and .tsv events do not match'

        # organise task events
        if event_model == 'motor':
            events = motor_model(event_files)
        elif event_model == 'reasoning':
            events = event_files.copy()
        
        # fit the model.
        model.fit(run_imgs=img_files, events=events)

        # get contrasts
        if event_model == 'motor':
            contrasts = motor_contrasts(model)
        elif event_model == 'reasoning':
            contrasts = reasoning_contrasts(model)

        # calculate z map and save
        for label, con in contrasts.items():
            z_map = model.compute_contrast(con)
            out_file = 'sub-'+subj+'_glm-'+event_model+'_contrast-'+label+'.nii.gz'
            nib.save(z_map, out_dir+out_file)
    except:
        print(subj+'!!! sub failed, probably bad data:')