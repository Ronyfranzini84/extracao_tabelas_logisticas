
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from pathlib import Path

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/tables")

    # Find the first table
    table = driver.find_element(By.ID, "table1")

    # Find all rows in the table body
    rows = table.find_elements(By.XPATH, ".//tbody/tr")

    data = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")

        values = [cell.text for cell in cells]

        data.append(values)

    # Convert to DataFrame
    df = pd.DataFrame(
        data,
        columns=[
            "Sobrenome",
            "Nome",
            "Email",
            "Valor",
            "Site",
            "Acoes"
        ]
    )

    print(df.to_string(index=False))

finally:
    driver.quit()



# Convert the price column to numbers
df["Valor"] = pd.to_numeric(
    df["Valor"].str.replace("$", "", regex=False)
)

# Create the output folder
output_folder = Path.home() / "Downloads" / "relatorios_logisticos"
output_folder.mkdir(parents=True, exist_ok=True)

# Define the Excel file path
file_path = output_folder / "relatorio_tabelas.xlsx"

# Export to Excel
df.to_excel(file_path, index=False)

# Display the results
print(df.to_string(index=False))
print("\nData types:")
print(df.dtypes)
print(f"\nExcel saved at: {file_path}")
