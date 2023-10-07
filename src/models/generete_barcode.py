import win32print
import win32ui
from PIL import Image, ImageWin
import os
import datetime
from barcode import generate
from barcode.writer import ImageWriter

def send_barCode_To_Printer(printer_name, file_name, pyhWidth, pyHeight):

    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    printer_size = hDC.GetDeviceCaps(pyhWidth), hDC.GetDeviceCaps(pyHeight)

    bmp = Image.open (file_name)
    if bmp.size[0] < bmp.size[1]:
        bmp = bmp.rotate (90)

    hDC.StartDoc (file_name)
    hDC.StartPage ()

    dib = ImageWin.Dib (bmp)
    x, y = 0, 0
    dib.draw (hDC.GetHandleOutput(), (x,y,printer_size[0],printer_size[1]))

    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()


def generete_barcode(barcode_string, app_path):

    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111
    printer_name_SmallOne = ""
    printer_name_BigOne = ""
    
    current_date = datetime.datetime.now().strftime("%Y_%m_%d___%H_%M_%S")
    barcode_image_output = os.path.join(app_path, 'barcodes\images', 'BarcodeImage___'+ current_date)
    barcode_image = generate(
                                'code128', 
                                str(barcode_string), 
                                writer=ImageWriter(), 
                                writer_options={"text_distance": 1.2, "font_size": 20, "module_width":0.3 }, 
                                output=barcode_image_output
                            )
    

    file_name = barcode_image_output + '.png'
    print(file_name)

    # #Small Printer
    # for i in range(8):
    #     send_barCode_To_Printer(printer_name_SmallOne, file_name, PHYSICALWIDTH, PHYSICALHEIGHT)
    
    # #Big Printer
    # send_barCode_To_Printer(printer_name_BigOne, file_name, PHYSICALWIDTH, PHYSICALHEIGHT)


