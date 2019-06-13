from PIL import Image
from PIL import ImageOps
from PIL import _imaging
import os
from subprocess import call
import easygui
import easygui as gui
import sys


class Strings:  #change name to strings
    OVERYLAY_PARAMS_ACT = 'OVERLAYMINMAX(1, 2.6, 100); OVERLAYTRANSPARENCYONBACKGROUND(20);'
    OVERYLAY_PARAMS_ACT_2 = 'OVERLAYMINMAX(1, 2.6, 100); OVERLAYTRANSPARENCYONBACKGROUND(20);'

    START_ROW = 'BEGIN RESETDEFAULTS;'

    QUIT_ROW = 'quit;'
    END_ROW = 'END.'
    VIEW_SETTINGS = 'COLORBARVISIBLE (FALSE); SLICETEXT (TRUE);'

    COLOR_OPTIONS = ['Red', 'Green', 'Blue', 'Violet [r+b]', 'Yellow', 'Cyan [g+b]', 'actc', '2winter', '3warm',
                     '4cool', 'gold', '5redyell', '6bluegrn']
    COLOR_DICT = {'1': 'Red', '3': 'Green', '2': 'Blue', '4': 'Violet [r+b]', '5': 'Yellow', '6': 'Cyan [g+b]',
                  '7': '1hot', '8': '2winter', '9': '3warm', '10': '4cool', '13': 'actc', '11': '3warm', '12': '3warm',
                  '14': '3warm', '15': '3warm', '27': 'actc', '33': 'actc'}

    DE_ACTIOVATION_LAYER_NAME = 'deact'
    FLIPED_NAME = 'Mirror_'
    IMAGES_SUBPATH_IN_VIEWER = 'figures'
    VIEWER_FOLDER = 'viewer'
    DE_ACTIVATION_NAME = 'deact'
    DE_ACTIVATION_NAME2 = '_neg'


from PIL import Image
from PIL import ImageOps
from PIL import _imaging
import os
from subprocess import call
import easygui
import easygui as gui
import sys


class Strings: # the name should be strings
    OVERYLAY_PARAMS_DEFUALT = 'OVERLAYMINMAX(1, 2.6, 100); OVERLAYTRANSPARENCYONBACKGROUND(20);'
    OVERYLAY_PARAMS_DEFUALT2 = 'OVERLAYMINMAX(1, 2.6, 100); OVERLAYTRANSPARENCYONBACKGROUND(20);'

    START_ROW = 'BEGIN RESETDEFAULTS;'

    QUIT_ROW = 'quit;'
    END_ROW = 'END.'
    VIEW_SETTINGS = 'COLORBARVISIBLE (FALSE); SLICETEXT (TRUE);'

    COLOR_OPTIONS = ['Red', 'Green', 'Blue', 'Violet [r+b]', 'Yellow', 'Cyan [g+b]', 'actc', '2winter', '3warm',
                     '4cool', 'gold', '5redyell', '6bluegrn']
    COLOR_DICT = {'1': 'Red', '3': 'Green', '2': 'Blue', '4': 'Violet [r+b]', '5': 'Yellow', '6': 'Cyan [g+b]',
                  '7': '1hot', '8': '2winter', '9': '3warm', '10': '4cool', '13': 'actc', '11': '3warm', '12': '3warm',
                  '14': '3warm', '15': '3warm', '27': 'actc', '33': 'actc'}

    DE_ACTIOVATION_LAYER_NAME = 'deact'
    FLIPED_NAME = 'Mirror_'
    IMAGES_SUBPATH_IN_VIEWER = 'figures'
    VIEWER_FOLDER = 'viewer'
    FIGURES_PATH = 'figures'
    DE_ACTIVATION_NAME = 'deact'
    DE_ACTIVATION_NAME2 = '_neg'




class Params :
    def __init__(self, anatomy_file, first_layer, second_layer, first_layer_color,
                          second_layer_color, first_min_Tscore, first_max_Tscore, second_min_Tscore, second_max_Tscore,
                          deactivation_first_layer, deactivation_second_layer, type, patient_imgs_path):
        self._anatomy = anatomy_file
        self._first_layer = first_layer
        self._second_layer = second_layer

        self._first_layer_color = first_layer_color
        self._second_layer_color = second_layer_color
        self._first_min_Tscore = first_min_Tscore
        self._first_max_Tscore = first_max_Tscore
        self._second_min_Tscore = second_min_Tscore
        self._second_max_Tscore = second_max_Tscore
        self._is_first_deactivation = deactivation_first_layer #holds true or false
        self._is_second_deactivation = deactivation_second_layer
        if type.lower() == 'eeg':
            self._is_eeg = True
        else:
            self._is_eeg = False
        self._imgs_path = patient_imgs_path




def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)



def build_gls_text (patient_params):

    anatomy_gls = 'LOADIMAGE(\''  + patient_params._anatomy + '\');'

    first_layer_name = patient_params._first_layer.split('\\')[-1].split('.')[0]
    #first_layer_name = first_layer_name.split('.')[0]
    first_layer_gls = 'OVERLAYLOAD(\''  + patient_params._first_layer + '\');'

    first_layer_color_gls = "OVERLAYCOLORNAME(1,'" + patient_params._first_layer_color +  "');"

    # set Tscore values
    if patient_params._is_eeg:
        if patient_params._is_first_deactivation or ( float(patient_params._first_min_Tscore)<0 and float(patient_params._first_max_Tscore)<=0 ):
            first_Tscore_gls = ('OVERLAYMINMAX(1,' + patient_params._first_max_Tscore + ',' + patient_params._first_min_Tscore + '); OVERLAYTRANSPARENCYONBACKGROUND(20);')
        else:
            first_Tscore_gls = ('OVERLAYMINMAX(1,' + '0.5' + ',' + patient_params._first_max_Tscore + '); OVERLAYTRANSPARENCYONBACKGROUND(20);')
    else:
        first_Tscore_gls = Strings.OVERYLAY_PARAMS_DEFUALT


    if patient_params._second_layer != None: #if there is a second layer do:
        second_layer_name = '_' + patient_params._second_layer.split('\\')[-1].split('.')[0]
        second_layer_gls = 'OVERLAYLOAD(\'' + patient_params._second_layer + '\');'


        second_layer_color_gls = "OVERLAYCOLORNAME(2,'" + patient_params._second_layer_color +  "');"

        if patient_params._is_eeg:
            if patient_params._is_second_deactivation or ( float(second_min_Tscore)<0 and float(second_max_Tscore)<=0 ) :
                second_Tscore_gls = 'OVERLAYMINMAX(2,' + patient_params._second_max_Tscore + ',' + patient_params._second_min_Tscore + '); OVERLAYTRANSPARENCYONBACKGROUND(20);'
            else:
                second_Tscore_gls = 'OVERLAYMINMAX(2,' + '0.5' + ',' + patient_params._second_max_Tscore + '); OVERLAYTRANSPARENCYONBACKGROUND(20);'
    else: # if there is not a second layer. do:
        second_Tscore_gls = Strings.OVERYLAY_PARAMS_DEFUALT2
        second_layer_name = ''

    save_bmp_sagRight_gls = Strings.VIEW_SETTINGS + 'SAVEBMP(\'' + patient_params._imgs_path +'\\'+ first_layer_name + second_layer_name +'_sagRight\');'
    save_bmp_sagLeft_gls = Strings.VIEW_SETTINGS + 'SAVEBMP(\'' + patient_params._imgs_path +'\\'+ first_layer_name + second_layer_name + '_sagLeft\');'
    save_bmp_cor_gls = Strings.VIEW_SETTINGS + 'SAVEBMP(\'' + patient_params._imgs_path +'\\'+ first_layer_name + second_layer_name + '_cor\');'
    save_bmp_ax_gls = Strings.VIEW_SETTINGS + 'SAVEBMP(\'' + patient_params._imgs_path +'\\'+ first_layer_name + second_layer_name + '_ax\');'

    eeg_slices_ax = 'MOSAIC(\' H0.25 V0.15 A 200;\
                -40 -35 -30 -25 -20;\
                -15 -10 -5 0 5;\
                10 15 20 25 30;\
                35 40 45 50 55;\
                60 65 70 75 80;\
                85 90 95 100 105;\
                \'); '
    fibers_slices_ax = 'MOSAIC(\'H 0.19 V0.18 A 200; -35 -32 -29 -26 -23 -20 -17 -14 ;-11 -8 -5 -2 1 4 7 10; 13 16 19 22 25 28 31 34; 37 40 43 46 49 52 55 58; 61 64 67 70 73 76 79 82; 85 88 91 94 97 100 103 106 \'); '
    fibers_slices_cor = 'MOSAIC(\'H 0.3 C 200; -45 -40 -35 -30 -25 -20; -15 -10 -5 0 5 10; 15 20 25 30 35 40; 45 50 55 60 65 70; 75 80 85 90 95 100 \'); '
    fibers_slices_sagRight = 'MOSAIC(\'H 0.25 S 200; 0 3 6 9 12 15; 18 21 24 27 30 33; 36 39 42 45 48 51; 54 57 60 63 66 69\'); '
    fibers_slices_sagLeft = 'MOSAIC(\'H 0.25 S 200; 0 -3 -6 -9 -12 -15; -18 -21 -24 -27 -30 -33; -36 -39 -42 -45 -48 -51; -54 -57 -60 -63 -66 -69 \'); '


    gls_text = []
    gls_text.append(Strings.START_ROW)
    gls_text.append( anatomy_gls )
    gls_text.append( first_layer_gls )
    gls_text.append( first_layer_color_gls )
    gls_text.append( first_Tscore_gls )



    if patient_params._second_layer != None:
        gls_text.append( second_layer_gls )
        gls_text.append( second_layer_color_gls )
        gls_text.append( second_Tscore_gls )

    if patient_params._is_eeg:
        gls_text.append(eeg_slices_ax)
        gls_text.append(save_bmp_ax_gls)

    else:
        gls_text.append(fibers_slices_ax)
        gls_text.append(save_bmp_ax_gls)

        gls_text.append(fibers_slices_cor)
        gls_text.append(save_bmp_cor_gls)

        gls_text.append(fibers_slices_sagRight)
        gls_text.append(save_bmp_sagRight_gls)

        gls_text.append(fibers_slices_sagLeft)
        gls_text.append(save_bmp_sagLeft_gls)


    if patient_params._is_eeg == False:
        gls_text.append(Strings.QUIT_ROW)

    gls_text.append(Strings.END_ROW)

    return gls_text, first_layer_name



def create_gls_file (gls_text, patient_viewer_path, first_layer_name):

    gls_file_name = patient_viewer_path + '\\gls_' + first_layer_name + '.gls'
    gls_file = open (gls_file_name , 'w')

    for row in gls_text:
        gls_file.writelines(row + '\n')


    gls_file.close();
    return gls_file.name


def run_gls_file (gls_file):
    call (gls_file,shell=True)

def flip_image (images_path):
    for img_name in os.listdir ( images_path ):
        if ('bmp' or 'jpg' or 'png' in img_name) and Strings.FLIPED_NAME not in img_name:
            img = Image.open( os.path.join(images_path, img_name) )
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            img.save( os.path.join(images_path, Strings.FLIPED_NAME + img_name) )


def main(patient_folder, anatomy_file, first_layer, first_layer_color, first_min_Tscore, first_max_Tscore,
         second_layer, second_layer_color, second_min_Tscore, second_max_Tscore, type):


    patient_viewer_path = os.path.join(patient_folder, Strings.VIEWER_FOLDER)

    ensure_dir( os.path.join(patient_viewer_path,Strings.IMAGES_SUBPATH_IN_VIEWER) )
    patient_imgs_path = os.path.join(patient_viewer_path, Strings.IMAGES_SUBPATH_IN_VIEWER)


    if gui.ynbox('Do you want to change the FIRST layer color?', ''):
        first_layer_color = gui.choicebox('', 'Choose layer color', Strings.COLOR_OPTIONS)
    else:
        first_layer_color = Strings.COLOR_DICT[first_layer_color]


    if second_layer.lower() == 'none':
        second_layer = None
        second_layer_color = None
    else:
        if gui.ynbox('Do you want to change the SECOND layer color?', ''):
            second_layer_color = gui.choicebox('', 'Choose layer color', Strings.COLOR_OPTIONS)
        else:
            second_layer_color = Strings.COLOR_DICT[second_layer_color]


    deactivation_first_layer = False
    deactivation_second_layer = False
    if type.lower() == 'eeg':
        if Strings.DE_ACTIVATION_NAME or Strings.DE_ACTIVATION_NAME2 in first_layer:
            deactivation_first_layer = True
        if Strings.DE_ACTIVATION_NAME or Strings.DE_ACTIVATION_NAME2 in  second_layer:
            deactivation_second_layer = True


    patient_params = Params (anatomy_file, first_layer, second_layer, first_layer_color, second_layer_color, first_min_Tscore, first_max_Tscore,
                                        second_min_Tscore, second_max_Tscore, deactivation_first_layer,
                                        deactivation_second_layer, type, patient_imgs_path)


    gls_text, first_layer_name = build_gls_text(patient_params)
    gls_file_name = create_gls_file (gls_text, patient_viewer_path, first_layer_name)
    run_gls_file(gls_file_name)
    flip_image(patient_imgs_path)



# main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
# folder |    anatomy |      layer |  second layer | first color | second color
