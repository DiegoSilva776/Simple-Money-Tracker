import os

# This pattern must be used in the .txt files that are going to be 
# cleaned to tag the document's sections
SECTION_OPENNING = '>>>---'
SECTION_CLOSING  = '---<<<'

fileContent = None
datasetFileNames = [
    'cat_baby_care.txt',
    'cat_bakery.txt',
    'cat_butchery.txt',
    'cat_clothes.txt',
    'cat_water.txt',
    'cat_education.txt',
    'cat_energy.txt',
    'cat_gas.txt',
    'cat_greenery.txt',
    'cat_health.txt',
    'cat_house_items.txt',
    'cat_house_rent.txt',
    'cat_internet.txt',
    'cat_phone.txt',
    'cat_recreation.txt',
    'cat_supermarket.txt',
    'cat_transport.txt'
]

for filename in datasetFileNames:
    print("Applying basic clean up algorithm to file: " + filename)

    # Read the file content and store the content it in memory :(, then erase the file
    with open(os.path.join(os.getcwd(), filename), 'r+') as f:
        fileContent = f.readlines()
        f.write('')

    # Clean each line of the content and write it back in the file
    with open(os.path.join(os.getcwd(), filename), 'r+') as f:
        cleanedLine = ''

        for line in fileContent:

            if line != '\n':

                try:

                    if line != SECTION_OPENNING or line != SECTION_CLOSING:
                        # Clean up undesired words
                        txt_cat_transport = line.replace('\n', '')
                        txt_cat_transport = txt_cat_transport.replace('\t', '')
                        txt_cat_transport = txt_cat_transport.replace('\"container\"', '')
                        txt_cat_transport = txt_cat_transport.replace('class=\"container', '')
                        txt_cat_transport = txt_cat_transport.replace('class=\"container', '')
                        txt_cat_transport = txt_cat_transport.replace('container-body', '')
                        txt_cat_transport = txt_cat_transport.replace('./container', '')

                        words = txt_cat_transport.split()
                        cleanedLine = ' '.join(words)
                    else:

                        if line == SECTION_OPENNING:
                            cleanedLine = '\n' + line + '\n'
                        else:
                            cleanedLine = line + '\n'

                    print(cleanedLine, file = f)

                except ValueError:
                    print("Failed to write this line into the file!")
