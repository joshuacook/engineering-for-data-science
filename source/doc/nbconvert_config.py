c = get_config()

c.NbConvertApp.notebooks = ['main.ipynb']
c.TagRemovePreprocessor.remove_cell_tags = {'remove'}
c.TagRemovePreprocessor.remove_input_tags = {'output_only'}
c.NbConvertApp.export_format = 'pdf'
c.Exporter.template_file = 'doc/custom'
c.PDFExporter.latex_command = ['xelatex', '{filename}']
c.PDFExporter.latex_count = 3
c.PDFExporter.temp_file_exts = ['.aux', '.bbl', '.blg', '.idx', '.log', '.out', '.tex']
c.PDFExporter.verbose = False
