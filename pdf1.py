from pypdf import (
   ObjectDeletionFlag,
   PageObject,
   PdfMerger,
   PdfReader,
   PdfWriter,
   Transformation,
)

from pypdf.generic import (
  ArrayObject,
  ContentStream,
  DictionaryObject,
  Fit,
  IndirectObject,
  NameObject,
  NumberObject,
  RectangleObject,
  StreamObject,
  TextStringObject,
)

def test_writer():
  src = "./test1.pdf"
  dst = "./test1_out.pdf"
  
  reader = PdfReader(open(src, `rb`))
  writer = PdfWriter()
  
  for page in range( len(reader.pages) ):
      writer.add_page ( reader.pages[page] )
      
 # add extra blank pages, if needed 
 # writer.add_blank_page(1223,791)   # width, height dpi
  
 to_add = [
   ("./test1.xls"),
   ("./test2.xls")
 ]

for file_name in to_add :
  print("/n .. adding and opening ", file_name)
  with open(file_name, `rb`) as fp:
      writer.add_attachment(file_name, fp.read() )
  fp.close()
  
# write output

 output_stream = open(dst, "wb")
    writer.write(output_stream)

 output_stream.close()

return

def main():
  
    print(" adding files ...")
    test_writer()
    
if __name__ == "__main__" :
     main()
    

                                 
