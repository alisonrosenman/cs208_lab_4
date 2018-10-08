#############################################
#
# Lab 4: Test and evaluate your ASR
# Team: 2
# Member Names: Alison Rosenman, Ricki Su, Vincent Yu
#
#############################################

# Complete this function - see the Lab 4 instructions


def calculate_errors(hyp, ref):
    # First, pre-process the given sentences
    hyp, ref = hyp.lower(), ref.lower()
    hyp, ref = hyp.split(), ref.split()
    assert len(hyp) != 0 and len(ref) != 0

    errors = 0

    while len(hyp) > 1 and len(ref) > 1:
        if hyp[0] != ref[0]:
            # Regardless of the error, add 1 to the total amount of errors.
            errors += 1
            if ref[0] in hyp[1:]:
                hyp = hyp[1:]
            elif hyp[0] in ref[1:]:
                ref = ref[1:]
            else:
                ref, hyp = ref[1:], hyp[1:]
        else:
            ref, hyp = ref[1:], hyp[1:]
    # By now, either one of the two has only 1 word left.
    if len(ref) == 1:
        if ref[0] in hyp:
            errors += (len(hyp) - 1)
        else:
            errors += len(hyp)
    if len(hyp) == 1:
        if hyp[0] in ref:
            errors += (len(ref) - 1)
        else:
            errors += len(ref)
    # Decrease the errors by since case overlaps.
    if (len(hyp) == len(ref)) and (hyp[0] != ref[0]):
        errors -= 1
    return errors


# Come up with five "reference" sentences you will use to test your ASR.

ref1 = 'I want to see Pulp Fiction at Narberth Cinema at noon'
ref2 = 'I want to see Inception at Bryn Mawr Film Institute at three PM'
ref3 = ''
ref4 = ''
ref5 = ''

# Enter total number of words for all of your reference sentences 
test_total_words = len(ref1.split()) + len(ref2.split()) + len(ref3.split()) + len(ref4.split()) + len(ref5.split())


# Use this function to test your calculate errors function - see the Lab 4 instructions.
def demo():
    pass


# This just ensures the demo will only be run if we run WER.py directly, since we're going to import it into another
# file eventually.
if __name__ == "__main__":
    demo()
