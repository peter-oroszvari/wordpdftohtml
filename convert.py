import mammoth

custom_styles = "b => i"

input_filename = "sample.docx"
custom_styles = "b => i"

with open(input_filename, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles)
    text = result.value
    with open('output.html', 'w') as html_file:
        html_file.write(text)