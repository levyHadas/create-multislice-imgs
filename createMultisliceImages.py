import os
import sys
import createMultisliceImages_full


if __name__ == '__main__':

    folder, anatomy, layer, first_color, first_min_Tscore, first_max_Tscore, second_layer, second_color, second_min_Tscore, second_max_Tscore = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]

    if 'spk' in layer.lower() or 'spike' in layer.lower() or 'Lag' in layer :
        type = ('eeg')
    else:
        type = 'fibers'


    createMultisliceImages_full.main(folder, anatomy, layer, first_color, first_min_Tscore, first_max_Tscore,
                                     second_layer, second_color, second_min_Tscore, second_max_Tscore, type)



