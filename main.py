# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import create_form
import fill_form


###
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_form.create_simple_form()
    fill_form.create_overlay()
    fill_form.merge_pdfs('simple_form_overlay.pdf', 'simple_form.pdf', 'merged_form.pdf')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
