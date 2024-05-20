import csv
import yaml

csv_file = 'projects.csv'
output_file = 'projects.markdown'

# Initialize data structure
data = {
    'layout': 'home',
    'title': 'Projects',
    'accordion': [],
    'accordion2': []
}

# Function to add non-empty values to the dictionary
def add_non_empty_fields(item, row, field_name, key_name):
    if row[field_name].strip():
        item[key_name] = row[field_name].strip()

# Read CSV and populate data structure
with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        item = {}
        add_non_empty_fields(item, row, 'Project Name', 'title')
        add_non_empty_fields(item, row, 'Description', 'description')
        add_non_empty_fields(item, row, 'PI', 'pi')
        add_non_empty_fields(item, row, 'Funder', 'funder')
        add_non_empty_fields(item, row, 'Technologies', 'tech')
        add_non_empty_fields(item, row, 'Links', 'links')

        if row['Current'] == '1':  # Assuming '1' is used to denote current projects
            data['accordion'].append(item)
        elif row['Current'] == '0':  # Assuming '0' is used to denote past projects
            data['accordion2'].append(item)

# Convert data to YAML format and write to file
with open(output_file, 'w') as file:
    file.write('---\n')
    yaml.dump(data, file, default_flow_style=False)
    file.write('---\n')

    # Add the static content below the front matter
    file.write("""
The team have worked on a number of projects in the past, and are always looking for new opportunities to collaborate.
Here are some of the projects we have worked on:

### Current projects:
<ul class="jekyllcodex_accordion">
    {% for item in page.accordion %}
    <li>
        <input id="accordion{{ forloop.index }}" type="checkbox" />
        <label for="accordion{{ forloop.index }}">
            {{ item.title }}
        </label>
        <div>
            <p>{{ item.description }}</p>
            <ul>
                {% if item.pi %}<li><strong>PI:</strong> {{ item.pi }}</li>{% endif %}
                {% if item.funder %}<li><strong>Funder:</strong> {{ item.funder }}</li>{% endif %}
                {% if item.tech %}<li><strong>Technologies:</strong> {{ item.tech }}</li>{% endif %}
                {% if item.links %}<li><strong>Links:</strong> {{ item.links }}</li>{% endif %}
            </ul>
        </div>
    </li>
    {% endfor %}
</ul>

### Past projects:
<ul class="jekyllcodex_accordion">
    {% for item in page.accordion2 %}
    <li>
        <input id="accordion2{{ forloop.index }}" type="checkbox" />
        <label for="accordion2{{ forloop.index }}">
            {{ item.title }}
        </label>
        <div>
            <p>{{ item.description }}</p>
            <ul>
                {% if item.pi %}<li><strong>PI:</strong> {{ item.pi }}</li>{% endif %}
                {% if item.funder %}<li><strong>Funder:</strong> {{ item.funder }}</li>{% endif %}
                {% if item.tech %}<li><strong>Technologies:</strong> {{ item.tech }}</li>{% endif %}
                {% if item.links %}<li><strong>Links:</strong> {{ item.links }}</li>{% endif %}
            </ul>
        </div>
    </li>
    {% endfor %}
</ul>

<style>
    ul.jekyllcodex_accordion {position: relative; margin: 1.4rem 0!important; border-bottom: 1px solid rgba(0,0,0,0.25); padding-bottom: 0;}
    ul.jekyllcodex_accordion > li {border-top: 1px solid rgba(0,0,0,0.25); list-style: none; margin-left: 0;}
    ul.jekyllcodex_accordion > li input {display: none;}
    ul.jekyllcodex_accordion > li label {display: block; cursor: pointer; padding: 0.75rem 2.4rem 0.75rem 0; margin: 0;}
    ul.jekyllcodex_accordion > li div {display: none; padding-bottom: 1.2rem;}
    ul.jekyllcodex_accordion > li input:checked + label {font-weight: bold;}
    ul.jekyllcodex_accordion > li input:checked + label + div {display: block;}
    ul.jekyllcodex_accordion > li label::before {content: "+"; font-weight: normal; font-size: 130%; line-height: 1.1rem; padding: 0; position: absolute; right: 0.5rem; transition: all 0.15s ease-in-out;}
    ul.jekyllcodex_accordion > li input:checked + label::before {transform: rotate(-45deg);}
</style>
    """)

print("Markdown file created successfully.")
