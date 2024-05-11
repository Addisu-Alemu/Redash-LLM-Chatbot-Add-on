import os
import openai
from secret_key import api_key





# Set your OpenAI API key
openai.api_key = api_key


# Define a function to generate SQL query from natural language input
def generate_sql_query(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that can translate natural language queries into SQL queries."},
        {"role": "user", "content": f"Translate the following natural language query into a SQL query:\n\n{prompt}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    sql_query = response.choices[0].message.content.strip()
    return sql_query

# Main loop
while True:
    natural_language_query = input("Enter a natural language query (or 'q' to quit): ")

    if natural_language_query.lower() == 'q':
        break

    sql_query = generate_sql_query(natural_language_query)
    print(f"Natural Language Query: {natural_language_query}")
    print(f"Generated SQL Query: {sql_query}")
    print()