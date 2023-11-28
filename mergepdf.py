from  pypdf import PdfMerger

finalpdf=['TTF.pdf', 'file.pdf']

merge=PdfMerger()

for file in finalpdf:
   merge.append(file)

merge.write('final.pdf')
merge.close()
