from time import strftime

def get_current_timestamp():
    return strftime('%Y%m%d_%H%M%S')

submission_fname = 'submissions/stacking_%s.csv' % get_current_timestamp()
print(submission_fname)

submission_df.to_csv(submission_fname, index=False)
