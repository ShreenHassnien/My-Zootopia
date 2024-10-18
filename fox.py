import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    # Load animal data from JSON file
    animals_data = load_data('animals_data.json')

    # Read the HTML template
    with open('animals_template.html', 'r') as template_file:
        html_template = template_file.read()

    # Generate a string with animal data
    output = ''  # define an empty string
    for animal_data in animals_data:
        # append information to each string
        output += '<li class="cards__item">'
        output += f"Name: {animal_data['name']}<br/>\n"
        output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
        ...
        output += '</li>'
    print(output)
    # Replace the placeholder in the template with the generated string
    final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

    # Write the new HTML content to a file
    with open('animals.html', 'w') as output_file:
        output_file.write(final_html)


if __name__ == "__main__":
    main()
