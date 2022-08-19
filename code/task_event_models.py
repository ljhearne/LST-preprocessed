import pandas as pd
import numpy as np


def motor_model(event_files):

    # organises task events according to model
    events = []
    for run in range(len(event_files)):

        # create model of button presses
        # this requires a little finagling because it is not
        # the typical GLM that BIDS is set up for
        df = pd.read_csv(event_files[run], delimiter='\t')

        new_df = pd.DataFrame(columns=['onset', 'duration', 'trial_type'])
        new_df['onset'] = df['motor_onset'].values
        new_df['trial_type'] = df['motor_key'].values
        new_df['duration'] = 2

        new_df = new_df.sort_values(by=['onset']).reset_index(drop=True)
        events.append(new_df)
    return events


def motor_contrasts(model):
    # create a condition dict
    empty_condition = np.zeros((model.design_matrices_[0].shape[1]))
    left_index = empty_condition.copy()
    left_index[0] = 3
    left_index[1:4] = -1

    left_middle = empty_condition.copy()
    left_middle[1] = 3
    left_middle[[0, 2, 3]] = -1

    right_index = empty_condition.copy()
    right_index[2] = 3
    right_index[[0, 1, 3]] = -1

    right_middle = empty_condition.copy()
    right_middle[3] = 3
    right_middle[0:3] = -1

    contrasts = {'leftindex': left_index,
                 'leftmiddle': left_middle,
                 'rightindex': right_index,
                 'rightmiddle': right_middle}
    return contrasts

def reasoning_contrasts(model):
    # create a condition dict
    empty_condition = np.zeros((model.design_matrices_[0].shape[1]))
    ter_minus_bin = empty_condition.copy()
    ter_minus_bin[3] = 1
    ter_minus_bin[0] = -1

    qua_minus_bin = empty_condition.copy()
    qua_minus_bin[2] = 1
    qua_minus_bin[0] = -1

    contrasts = {'ternary': ter_minus_bin,
                    'quaternary': qua_minus_bin}
    return contrasts