

def standard_combine_mult_and_diffref(mult, orig_inp, bg_data, return_mean: bool = True):
    to_return = [mult[l]*(orig_inp[l] - bg_data[l]) for l in range(len(orig_inp))]
    if return_mean:
        to_return = [x.mean(0) for x in to_return]
    return to_return
