from pywebio.input import textarea, input, input_group, select, NUMBER, actions
from pywebio import start_server
from pywebio.output import put_text
from fpdf import FPDF

FONTS = ['Helvetica', 'Calibri', 'Futura', 'Garamond', 'Times New Roman',
         'Arial', 'Cambria', 'Verdana', 'Rockwell', 'Franklin Gothic']


def app_main():
    add_more = True
    pages = []

    while add_more:
        page = textarea("Please insert the text for your PDF file",
                        placeholder="Type anything you like")
        pages.append(page)

        add_more = actions(label="Would you like to add another page?",
                           buttons=[{'label': 'Yes', 'value': True},
                                    {'label': 'No', 'value': False}])

    text_info = input_group('Text Fonts and Size', [
        select(label='Select your font', options=FONTS, value='Arial', name='font'),
        input("Select your text size", value='14', type=NUMBER, name='size')
    ])

    save_location = input("What is the name of your PDF file?")
    create_pdf(pages, text_info, save_location)
    put_text("Congratulations! A PDF file is generated for you.")


def create_page(pdf, text: str, font: str, size: int):
    pdf.add_page()
    pdf.set_font(font, '', size)  # Use the font and size provided

    lines = text.split('\n')
    for i, sent in enumerate(lines):
        pdf.cell(40, 10, sent, 0, i + 1)


def create_pdf(pages, text_info, save_location):
    pdf = FPDF()
    font = text_info['font']
    size = int(text_info['size'])  # Convert to integer

    for page in pages:
        create_page(pdf, page, font, size)

    pdf.output(save_location, 'F')

if __name__ == '__main__':
    start_server(app_main, port=8082, host="0.0.0.0", debug=True)

           
