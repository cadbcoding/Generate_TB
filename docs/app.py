from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Your existing function to generate unique values
def generate_unique_value(unique_values):
    multiple = random.randint(50, 100)
    value = -multiple * 1000
    
    while value in unique_values:
        multiple = random.randint(50, 100)
        value = -multiple * 1000
    
    unique_values.add(value)
    return value

# Route for handling form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        category_C_vars = ['C1', 'C2', 'C3', 'C4']
        variables_values = {}
        unique_values = set()

        for var in category_C_vars:
            value = generate_unique_value(unique_values)
            variables_values[var] = {'C': value}

        D_values = [-0.5 * c['C'] for c in variables_values.values()]
        B_values = [2 * c['C'] for c in variables_values.values()]
        A_values = [-2.5 * c['C'] for c in variables_values.values()]

        for i, (var, c_value) in enumerate(zip(category_C_vars, variables_values.values())):
            variables_values[var].update({
                'D': D_values[i],
                'B': B_values[i],
                'A': A_values[i]
            })

        total = sum(d['C'] + d['D'] + d['B'] + d['A'] for d in variables_values.values())
        return render_template('result.html', variables_values=variables_values, total=total)
    else:
        # Render index.html for GET requests
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
