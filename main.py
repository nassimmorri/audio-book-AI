import pyttsx3
import fitz  # PyMuPDF

# Initialize the text-to-speech engine
droid = pyttsx3.init()

# Prompt the user for their name
user_name = input("Enter your name: ")

# Greet the user with a personalized message
droid.say(f'Bonjour {user_name}, je suis un droid de la 3eme génération et je suis mariem')
droid.say('Maintenant tu peux te relaxer et écouter tranquillement')

# Open the PDF file using PyMuPDF (fitz)
pdf_file_path = 'cours-python.pdf'
livre = fitz.open(pdf_file_path)

# Get the number of pages in the PDF
pages = livre.page_count
print(f'Number of pages in the PDF: {pages}')

# Prompt the user for the page number they want to listen to
page_number = int(input(f"Enter the page number you want to listen to (1 - {pages}): "))

# Validate the input page number
if 1 <= page_number <= pages:
    # Get the selected page
    selected_page = livre[page_number - 1]

    # Extract text from the selected page
    texte = selected_page.get_text()

    # Use the text-to-speech engine to read the extracted text
    droid.say(texte)
    droid.runAndWait()
else:
    print("Invalid page number. Please enter a valid page number.")

# Close the PDF file
livre.close()
