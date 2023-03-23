from confluence import Confluence

# Set the path to the input Confluence Markup Language file
cml_file_path = 'input.cml'

# Set the path to the output HTML file
html_file_path = 'output.html'

# Initialize a Confluence object
confluence = Confluence()

# Load the Confluence Markup Language file
with open(cml_file_path, 'r') as cml_file:
    cml = cml_file.read()

# Convert the Confluence Markup Language to HTML
html = confluence.convert_storage_to_view(cml)

# Save the HTML to a file
with open(html_file_path, 'w') as html_file:
    html_file.write(html)
