# %%
import os
import json
import nibabel as nib
from nilearn.interfaces.bids import get_bids_files
from warnings import warn

class ImagingDataset:
    def __init__(self, subject_list, data_path):
        self.subject_list = subject_list
        self.data_path = data_path
        self.bids_path = data_path+'bids/'
        self.deriv_path = data_path+'derivatives/fmriprep/'

        if not os.path.exists(self.bids_path):
            raise ValueError('BIDS folder does not exist in given dataset')

        if not os.path.exists(self.deriv_path):
            raise ValueError('fmriprep folder does not exist in given dataset')

    def raw_subject_list(self):
        raw = [i.replace('sub-', '') for i in self.subject_list]
        return raw

    def get_tr_and_slice_time(self, subj, filters=None):
        ''' 
        Get tr and slice timing for subject.
        These are used for creating design matrices in
        nilearn.

        Assumes TR is same within subject (takes first scan)
        Assumes first subject, unless otherwise stated
        '''

        # get image specs
        img_specs = get_bids_files(self.deriv_path,
                                   modality_folder='func',
                                   file_tag='bold', 
                                   file_type='json',
                                   filters=filters,
                                   sub_label=subj)
        specs = json.load(open(img_specs[0], 'r'))  
        assert 'RepetitionTime' in specs
        t_r = float(specs['RepetitionTime'])

        if 'SliceTimingRef' in specs:
            slice_time_ref = float(specs['SliceTimingRef'])
        else:
            warn('SliceTimingRef not found, using 0.5')
            slice_time_ref = 0.5
        return t_r, slice_time_ref
